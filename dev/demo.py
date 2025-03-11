# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse
import asyncio
import sqlite3

import numpy as np
import sqlite_vec

from llama_stack.apis.vector_io import Chunk
from llama_stack.providers.inline.vector_io.sqlite_vec.sqlite_vec import SQLiteVecIndex

EMBEDDING_DIMENSION = 384
DB_PATH = ":memory:"
VECTOR_DB_ID = "vector_db"

conn = sqlite3.connect(DB_PATH)
conn.enable_load_extension(True)
sqlite_vec.load(conn)


async def setup_index():
    index = await SQLiteVecIndex.create(dimension=EMBEDDING_DIMENSION, connection=conn, bank_id=VECTOR_DB_ID)
    return index


sqlite_vec_index = asyncio.run(setup_index())

# Insert sample text chunks + embeddings
sample_chunks = [
    Chunk(content="Machine learning is transforming AI research.", metadata={"document_id": "doc-1"}),
    Chunk(content="Deep learning is a subset of machine learning.", metadata={"document_id": "doc-2"}),
    Chunk(content="Reinforcement learning helps train AI agents.", metadata={"document_id": "doc-3"}),
    Chunk(content="Vector search is useful for retrieving similar documents.", metadata={"document_id": "doc-4"}),
    Chunk(content="Neural networks are the backbone of deep learning.", metadata={"document_id": "doc-5"}),
]

np.random.seed(42)
sample_embeddings = np.array([np.random.rand(EMBEDDING_DIMENSION).astype(np.float32) for _ in sample_chunks])

asyncio.run(sqlite_vec_index.add_chunks(sample_chunks, sample_embeddings))


async def keyword_search(query_str, top_k=3):
    print(f"\n🔍 Keyword Search for: '{query_str}'")
    response = await sqlite_vec_index.query(
        embedding=None, query_str=query_str, k=top_k, score_threshold=0.0, search_mode="keyword"
    )
    for chunk, score in zip(response.chunks, response.scores, strict=False):
        print(f"📄 {chunk.metadata['document_id']}: {chunk.content} (Score: {score})")


async def vector_search(query_embedding, top_k=3):
    print("\n🔍 Vector Search Results:")
    response = await sqlite_vec_index.query(
        embedding=query_embedding, query_str="", k=top_k, score_threshold=0.0, search_mode="vector"
    )
    for chunk, score in zip(response.chunks, response.scores, strict=False):
        print(f"📄 {chunk.metadata['document_id']}: {chunk.content} (Score: {score:.4f})")


def main():
    parser = argparse.ArgumentParser(description="Vector and Keyword Search with SQLiteVec")
    parser.add_argument("--prompt", type=str, required=True, help="Query string for keyword search")
    args = parser.parse_args()

    asyncio.run(keyword_search(args.prompt))

    query_embedding = np.random.rand(EMBEDDING_DIMENSION).astype(np.float32)  # Replace with real embedding
    asyncio.run(vector_search(query_embedding))


if __name__ == "__main__":
    main()
    conn.close()
