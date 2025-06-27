# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import logging
import uuid
from typing import Any

from numpy.typing import NDArray
from qdrant_client import AsyncQdrantClient, models
from qdrant_client.models import PointStruct

from llama_stack.apis.files import Files
from llama_stack.apis.inference import InterleavedContent
from llama_stack.apis.vector_dbs import VectorDB
from llama_stack.apis.vector_io import (
    Chunk,
    QueryChunksResponse,
    SearchRankingOptions,
    VectorIO,
    VectorStoreChunkingStrategy,
    VectorStoreDeleteResponse,
    VectorStoreFileContentsResponse,
    VectorStoreFileObject,
    VectorStoreFileStatus,
    VectorStoreListFilesResponse,
    VectorStoreListResponse,
    VectorStoreObject,
    VectorStoreSearchResponsePage,
)
from llama_stack.providers.datatypes import Api, VectorDBsProtocolPrivate
from llama_stack.providers.inline.vector_io.qdrant import QdrantVectorIOConfig as InlineQdrantVectorIOConfig
from llama_stack.providers.utils.memory.openai_vector_store_mixin import OpenAIVectorStoreMixin
from llama_stack.providers.utils.memory.vector_store import (
    EmbeddingIndex,
    VectorDBWithIndex,
)

from .config import QdrantVectorIOConfig as RemoteQdrantVectorIOConfig

log = logging.getLogger(__name__)
CHUNK_ID_KEY = "_chunk_id"
OPENAI_VECTOR_STORES_METADATA_COLLECTION = "openai_vector_stores_metadata"


def convert_id(_id: str) -> str:
    """
    Converts any string into a UUID string based on a seed.

    Qdrant accepts UUID strings and unsigned integers as point ID.
    We use a seed to convert each string into a UUID string deterministically.
    This allows us to overwrite the same point with the original ID.
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, _id))


class QdrantIndex(EmbeddingIndex):
    def __init__(self, client: AsyncQdrantClient, collection_name: str, distance_metric: str = "COSINE"):
        self.client = client
        self.collection_name = collection_name
        self.distance_metric = distance_metric

    async def add_chunks(self, chunks: list[Chunk], embeddings: NDArray):
        assert len(chunks) == len(embeddings), (
            f"Chunk length {len(chunks)} does not match embedding length {len(embeddings)}"
        )

        if not await self.client.collection_exists(self.collection_name):
            # Get distance metric, defaulting to COSINE
            distance = getattr(models.Distance, self.distance_metric, models.Distance.COSINE)

            await self.client.create_collection(
                self.collection_name,
                vectors_config=models.VectorParams(size=len(embeddings[0]), distance=distance),
            )

        points = []
        for _i, (chunk, embedding) in enumerate(zip(chunks, embeddings, strict=False)):
            chunk_id = chunk.chunk_id
            points.append(
                PointStruct(
                    id=convert_id(chunk_id),
                    vector=embedding,
                    payload={"chunk_content": chunk.model_dump()} | {CHUNK_ID_KEY: chunk_id},
                )
            )

        await self.client.upsert(collection_name=self.collection_name, points=points)

    async def query_vector(self, embedding: NDArray, k: int, score_threshold: float) -> QueryChunksResponse:
        results = (
            await self.client.query_points(
                collection_name=self.collection_name,
                query=embedding.tolist(),
                limit=k,
                with_payload=True,
                score_threshold=score_threshold,
            )
        ).points

        chunks, scores = [], []
        for point in results:
            assert isinstance(point, models.ScoredPoint)
            assert point.payload is not None

            try:
                chunk = Chunk(**point.payload["chunk_content"])
            except Exception:
                log.exception("Failed to parse chunk")
                continue

            chunks.append(chunk)
            scores.append(point.score)

        return QueryChunksResponse(chunks=chunks, scores=scores)

    async def query_keyword(
        self,
        query_string: str,
        k: int,
        score_threshold: float,
    ) -> QueryChunksResponse:
        raise NotImplementedError("Keyword search is not supported in Qdrant")

    async def query_hybrid(
        self,
        embedding: NDArray,
        query_string: str,
        k: int,
        score_threshold: float,
        reranker_type: str,
        reranker_params: dict[str, Any] | None = None,
    ) -> QueryChunksResponse:
        raise NotImplementedError("Hybrid search is not supported in Qdrant")

    async def delete(self):
        await self.client.delete_collection(collection_name=self.collection_name)


class QdrantVectorIOAdapter(OpenAIVectorStoreMixin, VectorIO, VectorDBsProtocolPrivate):
    def __init__(
        self,
        config: RemoteQdrantVectorIOConfig | InlineQdrantVectorIOConfig,
        inference_api: Api.inference,
        files_api: Files | None,
    ) -> None:
        self.config = config
        self.client: AsyncQdrantClient = None
        self.cache = {}
        self.inference_api = inference_api
        self.files_api = files_api
        self.vector_db_store = None
        self.openai_vector_stores: dict[str, dict[str, Any]] = {}

    async def initialize(self) -> None:
        self.client = AsyncQdrantClient(**self.config.model_dump(exclude_none=True))
        # Load existing OpenAI vector stores using the mixin method
        self.openai_vector_stores = await self._load_openai_vector_stores()

    async def shutdown(self) -> None:
        await self.client.close()

    # OpenAI Vector Store Mixin abstract method implementations
    async def _save_openai_vector_store(self, store_id: str, store_info: dict[str, Any]) -> None:
        """Save vector store metadata to Qdrant collection metadata."""
        # Store metadata in a special collection for vector store metadata
        metadata_collection = OPENAI_VECTOR_STORES_METADATA_COLLECTION

        # Create metadata collection if it doesn't exist
        if not await self.client.collection_exists(metadata_collection):
            # Get distance metric from config, defaulting to COSINE for backward compatibility
            distance_metric = getattr(self.config, "distance_metric", "COSINE")
            distance = getattr(models.Distance, distance_metric, models.Distance.COSINE)

            await self.client.create_collection(
                collection_name=metadata_collection,
                vectors_config=models.VectorParams(size=1, distance=distance),
            )

        # Store metadata as a point with dummy vector
        await self.client.upsert(
            collection_name=metadata_collection,
            points=[
                models.PointStruct(
                    id=convert_id(store_id),
                    vector=[0.0],  # Dummy vector
                    payload={"metadata": store_info},
                )
            ],
        )

    async def _load_openai_vector_stores(self) -> dict[str, dict[str, Any]]:
        """Load all vector store metadata from Qdrant."""
        metadata_collection = OPENAI_VECTOR_STORES_METADATA_COLLECTION

        if not await self.client.collection_exists(metadata_collection):
            return {}

        # Get all points from metadata collection
        points = await self.client.scroll(
            collection_name=metadata_collection,
            limit=1000,  # Reasonable limit for metadata
            with_payload=True,
        )

        stores = {}
        for point in points[0]:  # points[0] contains the actual points
            if point.payload and "metadata" in point.payload:
                store_info = point.payload["metadata"]
                stores[store_info["id"]] = store_info

        return stores

    async def _update_openai_vector_store(self, store_id: str, store_info: dict[str, Any]) -> None:
        """Update vector store metadata in Qdrant."""
        await self._save_openai_vector_store(store_id, store_info)

    async def _delete_openai_vector_store_from_storage(self, store_id: str) -> None:
        """Delete vector store metadata from Qdrant."""
        metadata_collection = OPENAI_VECTOR_STORES_METADATA_COLLECTION

        if await self.client.collection_exists(metadata_collection):
            await self.client.delete(
                collection_name=metadata_collection, points_selector=models.PointIdsList(points=[convert_id(store_id)])
            )

    async def register_vector_db(
        self,
        vector_db: VectorDB,
    ) -> None:
        index = VectorDBWithIndex(
            vector_db=vector_db,
            index=QdrantIndex(self.client, vector_db.identifier, self.config.distance_metric),
            inference_api=self.inference_api,
        )

        self.cache[vector_db.identifier] = index

    async def unregister_vector_db(self, vector_db_id: str) -> None:
        if vector_db_id in self.cache:
            await self.cache[vector_db_id].index.delete()
            del self.cache[vector_db_id]

    async def _get_and_cache_vector_db_index(self, vector_db_id: str) -> VectorDBWithIndex | None:
        if vector_db_id in self.cache:
            return self.cache[vector_db_id]

        vector_db = await self.vector_db_store.get_vector_db(vector_db_id)
        if not vector_db:
            raise ValueError(f"Vector DB {vector_db_id} not found")

        index = VectorDBWithIndex(
            vector_db=vector_db,
            index=QdrantIndex(
                client=self.client, collection_name=vector_db.identifier, distance_metric=self.config.distance_metric
            ),
            inference_api=self.inference_api,
        )
        self.cache[vector_db_id] = index
        return index

    async def insert_chunks(
        self,
        vector_db_id: str,
        chunks: list[Chunk],
        ttl_seconds: int | None = None,
    ) -> None:
        index = await self._get_and_cache_vector_db_index(vector_db_id)
        if not index:
            raise ValueError(f"Vector DB {vector_db_id} not found")

        await index.insert_chunks(chunks)

    async def query_chunks(
        self,
        vector_db_id: str,
        query: InterleavedContent,
        params: dict[str, Any] | None = None,
    ) -> QueryChunksResponse:
        index = await self._get_and_cache_vector_db_index(vector_db_id)
        if not index:
            raise ValueError(f"Vector DB {vector_db_id} not found")

        return await index.query_chunks(query, params)

    async def openai_create_vector_store(
        self,
        name: str,
        file_ids: list[str] | None = None,
        expires_after: dict[str, Any] | None = None,
        chunking_strategy: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
        embedding_model: str | None = None,
        embedding_dimension: int | None = 384,
        provider_id: str | None = None,
        provider_vector_db_id: str | None = None,
    ) -> VectorStoreObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_list_vector_stores(
        self,
        limit: int | None = 20,
        order: str | None = "desc",
        after: str | None = None,
        before: str | None = None,
    ) -> VectorStoreListResponse:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_retrieve_vector_store(
        self,
        vector_store_id: str,
    ) -> VectorStoreObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_update_vector_store(
        self,
        vector_store_id: str,
        name: str | None = None,
        expires_after: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> VectorStoreObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_delete_vector_store(
        self,
        vector_store_id: str,
    ) -> VectorStoreDeleteResponse:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_search_vector_store(
        self,
        vector_store_id: str,
        query: str | list[str],
        filters: dict[str, Any] | None = None,
        max_num_results: int | None = 10,
        ranking_options: SearchRankingOptions | None = None,
        rewrite_query: bool | None = False,
        search_mode: str | None = "vector",
    ) -> VectorStoreSearchResponsePage:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_attach_file_to_vector_store(
        self,
        vector_store_id: str,
        file_id: str,
        attributes: dict[str, Any] | None = None,
        chunking_strategy: VectorStoreChunkingStrategy | None = None,
    ) -> VectorStoreFileObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_list_files_in_vector_store(
        self,
        vector_store_id: str,
        limit: int | None = 20,
        order: str | None = "desc",
        after: str | None = None,
        before: str | None = None,
        filter: VectorStoreFileStatus | None = None,
    ) -> VectorStoreListFilesResponse:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_retrieve_vector_store_file(
        self,
        vector_store_id: str,
        file_id: str,
    ) -> VectorStoreFileObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_retrieve_vector_store_file_contents(
        self,
        vector_store_id: str,
        file_id: str,
    ) -> VectorStoreFileContentsResponse:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_update_vector_store_file(
        self,
        vector_store_id: str,
        file_id: str,
        attributes: dict[str, Any] | None = None,
    ) -> VectorStoreFileObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")

    async def openai_delete_vector_store_file(
        self,
        vector_store_id: str,
        file_id: str,
    ) -> VectorStoreFileObject:
        raise NotImplementedError("OpenAI Vector Stores API is not supported in Qdrant")
