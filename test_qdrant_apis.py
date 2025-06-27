#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""
Test script to verify Qdrant vector IO APIs are working correctly
"""

import asyncio

import requests

# Server configuration
BASE_URL = "http://localhost:8321"
VECTOR_DBS_BASE = f"{BASE_URL}/v1/vector-dbs"  # Vector DBs use hyphens
VECTOR_IO_BASE = f"{BASE_URL}/v1/vector-io"  # Vector IO operations use hyphens
OPENAI_VECTOR_STORES_BASE = f"{BASE_URL}/v1/openai/v1/vector_stores"  # OpenAI vector stores


async def test_vector_io_apis():
    """Test the vector IO APIs"""

    print("🧪 Testing Qdrant Vector IO APIs...")
    print(f"Server URL: {BASE_URL}")
    print("-" * 50)

    # Test 1: Health check
    print("\n1. Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/v1/health")
        if response.status_code == 200:
            print("Health check passed")
        else:
            print(f"Health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"Health check error: {e}")
        return

    # Test 2: List vector DBs (should be empty initially)
    print("\n2. Testing list vector DBs...")
    try:
        response = requests.get(VECTOR_DBS_BASE)
        if response.status_code == 200:
            vector_dbs = response.json()
            print(f"List vector DBs successful: {len(vector_dbs.get('data', []))} DBs found")
            for db in vector_dbs.get("data", []):
                print(f"   - {db.get('identifier', 'Unknown')}")
        else:
            print(f"List vector DBs failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"List vector DBs error: {e}")

    # Test 3: Register a vector DB
    print("\n3. Testing register vector DB...")
    test_vector_db = {
        "vector_db_id": "test-qdrant-db",
        "embedding_model": "all-MiniLM-L6-v2",
        "embedding_dimension": 384,
    }

    try:
        response = requests.post(VECTOR_DBS_BASE, json=test_vector_db, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print("Register vector DB successful")
        else:
            print(f"Register vector DB failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"Register vector DB error: {e}")

    # Test 4: List vector DBs again (should now have one)
    print("\n4. Testing list vector DBs (after registration)...")
    try:
        response = requests.get(VECTOR_DBS_BASE)
        if response.status_code == 200:
            vector_dbs = response.json()
            print(f"List vector DBs successful: {len(vector_dbs.get('data', []))} DBs found")
            for db in vector_dbs.get("data", []):
                print(f"   - {db.get('identifier', 'Unknown')}")
        else:
            print(f"List vector DBs failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"List vector DBs error: {e}")

    # Test 5: Test OpenAI vector store APIs
    print("\n5. Testing OpenAI vector store APIs...")

    # Create a vector store
    vector_store_data = {"name": "test-store", "embedding_model": "all-MiniLM-L6-v2", "embedding_dimension": 384}

    try:
        response = requests.post(
            OPENAI_VECTOR_STORES_BASE, json=vector_store_data, headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            store_info = response.json()
            store_id = store_info.get("id")
            print(f"Create vector store successful: {store_id}")

            # List vector stores
            response = requests.get(OPENAI_VECTOR_STORES_BASE)
            if response.status_code == 200:
                stores = response.json()
                print(f"List vector stores successful: {len(stores.get('data', []))} stores found")
            else:
                print(f"List vector stores failed: {response.status_code}")
                print(f"   Response: {response.text}")

        else:
            print(f"Create vector store failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"Vector store API error: {e}")


if __name__ == "__main__":
    asyncio.run(test_vector_io_apis())
