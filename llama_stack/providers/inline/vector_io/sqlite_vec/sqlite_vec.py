# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import asyncio
import hashlib
import logging
import sqlite3
import struct
import uuid
from typing import Any, Dict, List, Optional

import numpy as np
import sqlite_vec
from numpy.typing import NDArray

from llama_stack.apis.inference.inference import Inference
from llama_stack.apis.vector_dbs import VectorDB
from llama_stack.apis.vector_io import Chunk, QueryChunksResponse, VectorIO
from llama_stack.providers.datatypes import VectorDBsProtocolPrivate
from llama_stack.providers.utils.memory.vector_store import EmbeddingIndex, VectorDBWithIndex

logger = logging.getLogger(__name__)

# Specifying search mode is dependent on the VectorIO provider.
VECTOR_SEARCH = "vector"
KEYWORD_SEARCH = "keyword"
SEARCH_MODES = {VECTOR_SEARCH, KEYWORD_SEARCH}


def serialize_vector(vector: List[float]) -> bytes:
    """Serialize a list of floats into a compact binary representation."""
    return struct.pack(f"{len(vector)}f", *vector)


def _create_sqlite_connection(db_path):
    """Create a SQLite connection with sqlite_vec extension loaded."""
    connection = sqlite3.connect(db_path)
    connection.enable_load_extension(True)
    sqlite_vec.load(connection)
    connection.enable_load_extension(False)
    return connection


class SQLiteVecIndex(EmbeddingIndex):
    """
    An index implementation that stores embeddings in a SQLite virtual table using sqlite-vec.
    Two tables are used:
      - A metadata table (chunks_{bank_id}) that holds the chunk JSON.
      - A virtual table (vec_chunks_{bank_id}) that holds the serialized vector.
      - An FTS5 table (fts_chunks_{bank_id}) for full-text keyword search.
    """

    def __init__(self, dimension: int, db_path: str, bank_id: str):
        self.dimension = dimension
        self.db_path = db_path
        self.bank_id = bank_id
        self.metadata_table = f"chunks_{bank_id}".replace("-", "_")
        self.vector_table = f"vec_chunks_{bank_id}".replace("-", "_")
        self.fts_table = f"fts_chunks_{bank_id}".replace("-", "_")

    @classmethod
    async def create(cls, dimension: int, db_path: str, bank_id: str):
        instance = cls(dimension, db_path, bank_id)
        await instance.initialize()
        return instance

    async def initialize(self) -> None:
        def _init_tables():
            connection = _create_sqlite_connection(self.db_path)
            cur = connection.cursor()
            try:
                # Create the table to store chunk metadata.
                cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {self.metadata_table} (
                        id TEXT PRIMARY KEY,
                        chunk TEXT
                    );
                """)
                # Create the virtual table for embeddings.
                cur.execute(f"""
                    CREATE VIRTUAL TABLE IF NOT EXISTS {self.vector_table}
                    USING vec0(embedding FLOAT[{self.dimension}], id TEXT);
                """)
                connection.commit()
                # FTS5 table (for keyword search) - creating both the tables by default. Will use the relevant one
                # based on query. Implementation of the change on client side will allow passing the search_mode option
                # during initialization to make it easier to create the table that is required.
                cur.execute(f"""
                            CREATE VIRTUAL TABLE IF NOT EXISTS {self.fts_table}
                            USING fts5(id, content);
                        """)
                connection.commit()
            finally:
                cur.close()
                connection.close()

        await asyncio.to_thread(_init_tables)

    async def delete(self) -> None:
        def _drop_tables():
            connection = _create_sqlite_connection(self.db_path)
            cur = connection.cursor()
            try:
                cur.execute(f"DROP TABLE IF EXISTS {self.metadata_table};")
                cur.execute(f"DROP TABLE IF EXISTS {self.vector_table};")
                cur.execute(f"DROP TABLE IF EXISTS {self.fts_table};")
                connection.commit()
            finally:
                cur.close()
                connection.close()

        await asyncio.to_thread(_drop_tables)

    async def add_chunks(self, chunks: List[Chunk], embeddings: NDArray, batch_size: int = 500):
        """
        Add new chunks along with their embeddings using batch inserts.
        For each chunk, we insert its JSON into the metadata table and then insert its
        embedding (serialized to raw bytes) into the virtual table using the assigned rowid.
        If any insert fails, the transaction is rolled back to maintain consistency.
        Also inserts chunk content into FTS table for keyword search support.
        """
        assert all(isinstance(chunk.content, str) for chunk in chunks), "SQLiteVecIndex only supports text chunks"

        def _execute_all_batch_inserts():
            connection = _create_sqlite_connection(self.db_path)
            cur = connection.cursor()

            try:
                cur.execute("BEGIN TRANSACTION")
                for i in range(0, len(chunks), batch_size):
                    batch_chunks = chunks[i : i + batch_size]
                    batch_embeddings = embeddings[i : i + batch_size]

                    # Insert metadata
                    metadata_data = [
                        (generate_chunk_id(chunk.metadata["document_id"], chunk.content), chunk.model_dump_json())
                        for chunk in batch_chunks
                    ]
                    cur.executemany(
                        f"""
                        INSERT INTO {self.metadata_table} (id, chunk)
                        VALUES (?, ?)
                        ON CONFLICT(id) DO UPDATE SET chunk = excluded.chunk;
                        """,
                        metadata_data,
                    )

                    # Insert vector embeddings
                    embedding_data = [
                        (
                            (
                                generate_chunk_id(chunk.metadata["document_id"], chunk.content),
                                serialize_vector(emb.tolist()),
                            )
                        )
                        for chunk, emb in zip(batch_chunks, batch_embeddings, strict=True)
                    ]
                    cur.executemany(
                        f"INSERT INTO {self.vector_table} (id, embedding) VALUES (?, ?);",
                        embedding_data,
                    )

                    # Insert FTS content
                    fts_data = [
                        (generate_chunk_id(chunk.metadata["document_id"], chunk.content), chunk.content)
                        for chunk in batch_chunks
                    ]
                    # DELETE existing entries with same IDs (FTS5 doesn't support ON CONFLICT)
                    cur.executemany(
                        f"DELETE FROM {self.fts_table} WHERE id = ?;",
                        [(row[0],) for row in fts_data],
                    )

                    # INSERT new entries
                    cur.executemany(
                        f"INSERT INTO {self.fts_table} (id, content) VALUES (?, ?);",
                        fts_data,
                    )

                connection.commit()

            except sqlite3.Error as e:
                connection.rollback()
                logger.error(f"Error inserting chunk batch: {e}")
                raise

            finally:
                cur.close()
                connection.close()

        # Run batch insertion in a background thread
        await asyncio.to_thread(_execute_all_batch_inserts)

    async def query(
        self,
        embedding: Optional[NDArray],
        query_string: Optional[str],
        k: int,
        score_threshold: float,
        mode: Optional[str],
    ) -> QueryChunksResponse:
        """
        Supports both vector-based and keyword-based searches.

        1. Vector Search (`mode=VECTOR_SEARCH`):
           Uses a virtual table for vector similarity, joined with metadata.

        2. Keyword Search (`mode=KEYWORD_SEARCH`):
           Uses SQLite FTS5 for relevance-ranked full-text search.
        """

        def _execute_query():
            connection = _create_sqlite_connection(self.db_path)
            cur = connection.cursor()

            try:
                if mode == VECTOR_SEARCH:
                    if embedding is None:
                        raise ValueError("embedding is required for vector search.")
                    emb_list = embedding.tolist() if isinstance(embedding, np.ndarray) else list(embedding)
                    emb_blob = serialize_vector(emb_list)

                    query_sql = f"""
                        SELECT m.id, m.chunk, v.distance
                        FROM {self.vector_table} AS v
                        JOIN {self.metadata_table} AS m ON m.id = v.id
                        WHERE v.embedding MATCH ? AND k = ?
                        ORDER BY v.distance;
                    """
                    cur.execute(query_sql, (emb_blob, k))

                elif mode == KEYWORD_SEARCH:
                    if query_string is None:
                        raise ValueError("query_string is required for keyword search.")

                    query_sql = f"""
                        SELECT DISTINCT m.id, m.chunk, bm25({self.fts_table}) AS score
                        FROM {self.fts_table} AS f
                        JOIN {self.metadata_table} AS m ON m.id = f.id
                        WHERE f.content MATCH ?
                        ORDER BY score ASC
                        LIMIT ?;
                    """
                    cur.execute(query_sql, (query_string, k))

                else:
                    raise ValueError(f"Invalid search_mode: {mode} please select from {SEARCH_MODES}")

                return cur.fetchall()
            finally:
                cur.close()
                connection.close()

        rows = await asyncio.to_thread(_execute_query)

        chunks, scores = [], []
        for row in rows:
            if mode == VECTOR_SEARCH:
                _id, chunk_json, distance = row
                score = 1.0 / distance if distance != 0 else float("inf")

                if score < score_threshold:
                    continue
            else:
                _id, chunk_json, score = row

            try:
                chunk = Chunk.model_validate_json(chunk_json)
            except Exception as e:
                logger.error(f"Error parsing chunk JSON for id {_id}: {e}")
                continue

            chunks.append(chunk)
            scores.append(score)

        return QueryChunksResponse(chunks=chunks, scores=scores)


class SQLiteVecVectorIOAdapter(VectorIO, VectorDBsProtocolPrivate):
    """
    A VectorIO implementation using SQLite + sqlite_vec.
    This class handles vector database registration (with metadata stored in a table named `vector_dbs`)
    and creates a cache of VectorDBWithIndex instances (each wrapping a SQLiteVecIndex).
    """

    def __init__(self, config, inference_api: Inference) -> None:
        self.config = config
        self.inference_api = inference_api
        self.cache: Dict[str, VectorDBWithIndex] = {}

    async def initialize(self) -> None:
        def _setup_connection():
            # Open a connection to the SQLite database (the file is specified in the config).
            connection = _create_sqlite_connection(self.config.db_path)
            cur = connection.cursor()
            try:
                # Create a table to persist vector DB registrations.
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS vector_dbs (
                        id TEXT PRIMARY KEY,
                        metadata TEXT
                    );
                """)
                connection.commit()
                # Load any existing vector DB registrations.
                cur.execute("SELECT metadata FROM vector_dbs")
                rows = cur.fetchall()
                return rows
            finally:
                cur.close()
                connection.close()

        rows = await asyncio.to_thread(_setup_connection)
        for row in rows:
            vector_db_data = row[0]
            vector_db = VectorDB.model_validate_json(vector_db_data)
            index = await SQLiteVecIndex.create(
                vector_db.embedding_dimension, self.config.db_path, vector_db.identifier
            )
            self.cache[vector_db.identifier] = VectorDBWithIndex(vector_db, index, self.inference_api)

    async def shutdown(self) -> None:
        # nothing to do since we don't maintain a persistent connection
        pass

    async def register_vector_db(self, vector_db: VectorDB) -> None:
        def _register_db():
            connection = _create_sqlite_connection(self.config.db_path)
            cur = connection.cursor()
            try:
                cur.execute(
                    "INSERT OR REPLACE INTO vector_dbs (id, metadata) VALUES (?, ?)",
                    (vector_db.identifier, vector_db.model_dump_json()),
                )
                connection.commit()
            finally:
                cur.close()
                connection.close()

        await asyncio.to_thread(_register_db)
        index = await SQLiteVecIndex.create(vector_db.embedding_dimension, self.config.db_path, vector_db.identifier)
        self.cache[vector_db.identifier] = VectorDBWithIndex(vector_db, index, self.inference_api)

    async def list_vector_dbs(self) -> List[VectorDB]:
        return [v.vector_db for v in self.cache.values()]

    async def unregister_vector_db(self, vector_db_id: str) -> None:
        if vector_db_id not in self.cache:
            logger.warning(f"Vector DB {vector_db_id} not found")
            return
        await self.cache[vector_db_id].index.delete()
        del self.cache[vector_db_id]

        def _delete_vector_db_from_registry():
            connection = _create_sqlite_connection(self.config.db_path)
            cur = connection.cursor()
            try:
                cur.execute("DELETE FROM vector_dbs WHERE id = ?", (vector_db_id,))
                connection.commit()
            finally:
                cur.close()
                connection.close()

        await asyncio.to_thread(_delete_vector_db_from_registry)

    async def insert_chunks(self, vector_db_id: str, chunks: List[Chunk], ttl_seconds: Optional[int] = None) -> None:
        if vector_db_id not in self.cache:
            raise ValueError(f"Vector DB {vector_db_id} not found. Found: {list(self.cache.keys())}")
        # The VectorDBWithIndex helper is expected to compute embeddings via the inference_api
        # and then call our index's add_chunks.
        await self.cache[vector_db_id].insert_chunks(chunks)

    async def query_chunks(
        self, vector_db_id: str, query: Any, params: Optional[Dict[str, Any]] = None
    ) -> QueryChunksResponse:
        if vector_db_id not in self.cache:
            raise ValueError(f"Vector DB {vector_db_id} not found")
        return await self.cache[vector_db_id].query_chunks(query, params)


def generate_chunk_id(document_id: str, chunk_text: str) -> str:
    """Generate a unique chunk ID using a hash of document ID and chunk text."""
    hash_input = f"{document_id}:{chunk_text}".encode("utf-8")
    return str(uuid.UUID(hashlib.md5(hash_input).hexdigest()))
