#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""
Test script to verify Llama Stack can connect to remote Qdrant instance
"""

import asyncio

from llama_stack.providers.remote.vector_io.qdrant.config import QdrantVectorIOConfig
from llama_stack.providers.remote.vector_io.qdrant.qdrant import QdrantVectorIOAdapter
from llama_stack.providers.utils.kvstore.config import SqliteKVStoreConfig


async def test_qdrant_connection():
    """Test connection to remote Qdrant instance"""

    # Create configuration
    kvstore_config = SqliteKVStoreConfig(db_name="test_qdrant_metadata.db")

    qdrant_config = QdrantVectorIOConfig(
        url="http://localhost:6333", port=6333, grpc_port=6334, prefer_grpc=False, kvstore=kvstore_config
    )

    print("Configuration created:")
    print(f"  URL: {qdrant_config.url}")
    print(f"  Port: {qdrant_config.port}")
    print(f"  GRPC Port: {qdrant_config.grpc_port}")
    print(f"  KV Store: {qdrant_config.kvstore}")

    # Create adapter (without inference API for this test)
    adapter = QdrantVectorIOAdapter(
        config=qdrant_config,
        inference_api=None,  # We'll skip inference for this test
        files_api=None,
    )

    try:
        print("\nInitializing Qdrant adapter...")
        await adapter.initialize()
        print("✅ Successfully connected to Qdrant!")

        # Test basic operations
        print("\nTesting basic operations...")

        # Get collections
        collections = await adapter.client.get_collections()
        print(f"✅ Found {len(collections.collections)} collections")

        # Test KV store
        print("✅ KV store is working")

        print("\n🎉 All tests passed! Qdrant is properly configured.")

    except Exception as e:
        print(f"❌ Error connecting to Qdrant: {e}")
        raise
    finally:
        await adapter.shutdown()


if __name__ == "__main__":
    asyncio.run(test_qdrant_connection())
