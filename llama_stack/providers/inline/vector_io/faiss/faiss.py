# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import asyncio
import base64
import io
import json
import logging
from typing import Any

import faiss
import numpy as np
from numpy.typing import NDArray

from llama_stack.apis.files import Files
from llama_stack.apis.inference import Inference, InterleavedContent
from llama_stack.apis.vector_dbs import VectorDB
from llama_stack.apis.vector_io import (
    Chunk,
    QueryChunksResponse,
    VectorIO,
)
from llama_stack.providers.datatypes import (
    HealthResponse,
    HealthStatus,
    VectorDBsProtocolPrivate,
)
from llama_stack.providers.utils.kvstore import kvstore_impl
from llama_stack.providers.utils.kvstore.api import KVStore
from llama_stack.providers.utils.memory.openai_vector_store_mixin import OpenAIVectorStoreMixin
from llama_stack.providers.utils.memory.vector_store import (
    EmbeddingIndex,
    VectorDBWithIndex,
)

from .config import FaissVectorIOConfig

logger = logging.getLogger(__name__)

VERSION = "v3"
VECTOR_DBS_PREFIX = f"vector_dbs:{VERSION}::"
FAISS_INDEX_PREFIX = f"faiss_index:{VERSION}::"
OPENAI_VECTOR_STORES_PREFIX = f"openai_vector_stores:{VERSION}::"
OPENAI_VECTOR_STORES_FILES_PREFIX = f"openai_vector_stores_files:{VERSION}::"
OPENAI_VECTOR_STORES_FILES_CONTENTS_PREFIX = f"openai_vector_stores_files_contents:{VERSION}::"


class FaissIndex(EmbeddingIndex):
    def __init__(self, dimension: int, kvstore: KVStore | None = None, bank_id: str | None = None):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunk_by_index: dict[int, Chunk] = {}
        self.kvstore = kvstore
        self.bank_id = bank_id

    @classmethod
    async def create(cls, dimension: int, kvstore: KVStore | None = None, bank_id: str | None = None):
        instance = cls(dimension, kvstore, bank_id)
        await instance.initialize()
        return instance

    async def initialize(self) -> None:
        if not self.kvstore:
            return

        index_key = f"{FAISS_INDEX_PREFIX}{self.bank_id}"
        stored_data = await self.kvstore.get(index_key)

        if stored_data:
            data = json.loads(stored_data)
            self.chunk_by_index = {int(k): Chunk.model_validate_json(v) for k, v in data["chunk_by_index"].items()}

            buffer = io.BytesIO(base64.b64decode(data["faiss_index"]))
            try:
                self.index = faiss.deserialize_index(np.load(buffer, allow_pickle=False))
            except Exception as e:
                logger.debug(e, exc_info=True)
                raise ValueError(
                    "Error deserializing Faiss index from storage. If you recently upgraded your Llama Stack, Faiss, "
                    "or NumPy versions, you may need to delete the index and re-create it again or downgrade versions.\n"
                    f"The problematic index is stored in the key value store {self.kvstore} under the key '{index_key}'."
                ) from e

    async def _save_index(self):
        if not self.kvstore or not self.bank_id:
            return

        np_index = faiss.serialize_index(self.index)
        buffer = io.BytesIO()
        np.save(buffer, np_index, allow_pickle=False)
        data = {
            "chunk_by_index": {k: v.model_dump_json() for k, v in self.chunk_by_index.items()},
            "faiss_index": base64.b64encode(buffer.getvalue()).decode("utf-8"),
        }

        index_key = f"{FAISS_INDEX_PREFIX}{self.bank_id}"
        await self.kvstore.set(key=index_key, value=json.dumps(data))

    async def delete(self):
        if not self.kvstore or not self.bank_id:
            return

        await self.kvstore.delete(f"{FAISS_INDEX_PREFIX}{self.bank_id}")

    async def add_chunks(self, chunks: list[Chunk], embeddings: NDArray, metadata: dict[str, Any] | None = None):
        # Add dimension check
        embedding_dim = embeddings.shape[1] if len(embeddings.shape) > 1 else embeddings.shape[0]
        if embedding_dim != self.index.d:
            raise ValueError(f"Embedding dimension mismatch. Expected {self.index.d}, got {embedding_dim}")

        indexlen = len(self.chunk_by_index)
        for i, chunk in enumerate(chunks):
            self.chunk_by_index[indexlen + i] = chunk

        self.index.add(np.array(embeddings).astype(np.float32))

        # Save updated index
        await self._save_index()

    async def query_vector(
        self,
        embedding: NDArray,
        k: int,
        score_threshold: float,
    ) -> QueryChunksResponse:
        distances, indices = await asyncio.to_thread(self.index.search, embedding.reshape(1, -1).astype(np.float32), k)
        chunks = []
        scores = []
        for d, i in zip(distances[0], indices[0], strict=False):
            if i < 0:
                continue
            chunks.append(self.chunk_by_index[int(i)])
            scores.append(1.0 / float(d) if d != 0 else float("inf"))

        return QueryChunksResponse(chunks=chunks, scores=scores)

    async def query_keyword(
        self,
        query_string: str,
        k: int,
        score_threshold: float,
    ) -> QueryChunksResponse:
        raise NotImplementedError("Keyword search is not supported in FAISS")

    async def query_hybrid(
        self,
        embedding: NDArray,
        query_string: str,
        k: int,
        score_threshold: float,
        reranker_type: str,
        reranker_params: dict[str, Any] | None = None,
    ) -> QueryChunksResponse:
        raise NotImplementedError("Hybrid search is not supported in FAISS")


class FaissVectorIOAdapter(OpenAIVectorStoreMixin, VectorIO, VectorDBsProtocolPrivate):
    def __init__(self, config: FaissVectorIOConfig, inference_api: Inference, files_api: Files | None) -> None:
        self.config = config
        self.inference_api = inference_api
        self.files_api = files_api
        self.cache: dict[str, VectorDBWithIndex] = {}
        self.kvstore: KVStore | None = None
        self.openai_vector_stores: dict[str, dict[str, Any]] = {}

    async def initialize(self) -> None:
        self.kvstore = await kvstore_impl(self.config.kvstore)
        # Load existing banks from kvstore
        start_key = VECTOR_DBS_PREFIX
        end_key = f"{VECTOR_DBS_PREFIX}\xff"
        stored_vector_dbs = await self.kvstore.values_in_range(start_key, end_key)

        for vector_db_data in stored_vector_dbs:
            vector_db = VectorDB.model_validate_json(vector_db_data)
            index = VectorDBWithIndex(
                vector_db,
                await FaissIndex.create(vector_db.embedding_dimension, self.kvstore, vector_db.identifier),
                self.inference_api,
            )
            self.cache[vector_db.identifier] = index

        # Load existing OpenAI vector stores using the mixin method
        self.openai_vector_stores = await self._load_openai_vector_stores()

    async def shutdown(self) -> None:
        # Cleanup if needed
        pass

    async def health(self) -> HealthResponse:
        """
        Performs a health check by verifying connectivity to the inline faiss DB.
        This method is used by the Provider API to verify
        that the service is running correctly.
        Returns:

            HealthResponse: A dictionary containing the health status.
        """
        try:
            vector_dimension = 128  # sample dimension
            faiss.IndexFlatL2(vector_dimension)
            return HealthResponse(status=HealthStatus.OK)
        except Exception as e:
            return HealthResponse(status=HealthStatus.ERROR, message=f"Health check failed: {str(e)}")

    async def register_vector_db(
        self,
        vector_db: VectorDB,
    ) -> None:
        assert self.kvstore is not None

        key = f"{VECTOR_DBS_PREFIX}{vector_db.identifier}"
        await self.kvstore.set(
            key=key,
            value=vector_db.model_dump_json(),
        )

        # Store in cache
        self.cache[vector_db.identifier] = VectorDBWithIndex(
            vector_db=vector_db,
            index=await FaissIndex.create(vector_db.embedding_dimension, self.kvstore, vector_db.identifier),
            inference_api=self.inference_api,
        )

    async def list_vector_dbs(self) -> list[VectorDB]:
        return [i.vector_db for i in self.cache.values()]

    async def unregister_vector_db(self, vector_db_id: str) -> None:
        assert self.kvstore is not None

        if vector_db_id not in self.cache:
            logger.warning(f"Vector DB {vector_db_id} not found")
            return

        await self.cache[vector_db_id].index.delete()
        del self.cache[vector_db_id]
        await self.kvstore.delete(f"{VECTOR_DBS_PREFIX}{vector_db_id}")

    async def insert_chunks(
        self,
        vector_db_id: str,
        chunks: list[Chunk],
        ttl_seconds: int | None = None,
        params: dict[str, Any] | None = None,
    ) -> None:
        index = self.cache.get(vector_db_id)
        if index is None:
            raise ValueError(f"Vector DB {vector_db_id} not found. found: {self.cache.keys()}")

        await index.insert_chunks(chunks)

    async def query_chunks(
        self,
        vector_db_id: str,
        query: InterleavedContent,
        params: dict[str, Any] | None = None,
    ) -> QueryChunksResponse:
        index = self.cache.get(vector_db_id)
        if index is None:
            raise ValueError(f"Vector DB {vector_db_id} not found")

        return await index.query_chunks(query, params)

    # OpenAI Vector Store Mixin abstract method implementations
    async def _save_openai_vector_store(self, store_id: str, store_info: dict[str, Any]) -> None:
        """Save vector store metadata to kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_PREFIX}{store_id}"
        await self.kvstore.set(key=key, value=json.dumps(store_info))

    async def _load_openai_vector_stores(self) -> dict[str, dict[str, Any]]:
        """Load all vector store metadata from kvstore."""
        assert self.kvstore is not None
        start_key = OPENAI_VECTOR_STORES_PREFIX
        end_key = f"{OPENAI_VECTOR_STORES_PREFIX}\xff"
        stored_openai_stores = await self.kvstore.values_in_range(start_key, end_key)

        stores = {}
        for store_data in stored_openai_stores:
            store_info = json.loads(store_data)
            stores[store_info["id"]] = store_info
        return stores

    async def _update_openai_vector_store(self, store_id: str, store_info: dict[str, Any]) -> None:
        """Update vector store metadata in kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_PREFIX}{store_id}"
        await self.kvstore.set(key=key, value=json.dumps(store_info))

    async def _delete_openai_vector_store_from_storage(self, store_id: str) -> None:
        """Delete vector store metadata from kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_PREFIX}{store_id}"
        await self.kvstore.delete(key)

    async def _save_openai_vector_store_file(
        self, store_id: str, file_id: str, file_info: dict[str, Any], file_contents: list[dict[str, Any]]
    ) -> None:
        """Save vector store file metadata to kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_FILES_PREFIX}{store_id}:{file_id}"
        await self.kvstore.set(key=key, value=json.dumps(file_info))
        content_key = f"{OPENAI_VECTOR_STORES_FILES_CONTENTS_PREFIX}{store_id}:{file_id}"
        await self.kvstore.set(key=content_key, value=json.dumps(file_contents))

    async def _load_openai_vector_store_file(self, store_id: str, file_id: str) -> dict[str, Any]:
        """Load vector store file metadata from kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_FILES_PREFIX}{store_id}:{file_id}"
        stored_data = await self.kvstore.get(key)
        return json.loads(stored_data) if stored_data else {}

    async def _load_openai_vector_store_file_contents(self, store_id: str, file_id: str) -> list[dict[str, Any]]:
        """Load vector store file contents from kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_FILES_CONTENTS_PREFIX}{store_id}:{file_id}"
        stored_data = await self.kvstore.get(key)
        return json.loads(stored_data) if stored_data else []

    async def _update_openai_vector_store_file(self, store_id: str, file_id: str, file_info: dict[str, Any]) -> None:
        """Update vector store file metadata in kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_FILES_PREFIX}{store_id}:{file_id}"
        await self.kvstore.set(key=key, value=json.dumps(file_info))

    async def _delete_openai_vector_store_file_from_storage(self, store_id: str, file_id: str) -> None:
        """Delete vector store file metadata from kvstore."""
        assert self.kvstore is not None
        key = f"{OPENAI_VECTOR_STORES_FILES_PREFIX}{store_id}:{file_id}"
        await self.kvstore.delete(key)
