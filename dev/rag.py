# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os
import uuid

from llama_stack_client.types import Document

from llama_stack.apis.tools import RAGQueryConfig


def create_http_client():
    from llama_stack_client import LlamaStackClient

    return LlamaStackClient(base_url=f"http://localhost:{os.environ['LLAMA_STACK_PORT']}")


def create_library_client(template="ollama"):
    from llama_stack import LlamaStackAsLibraryClient

    client = LlamaStackAsLibraryClient(template)
    client.initialize()
    return client


client = create_library_client()  # or create_http_client() depending on the environment you picked

# Documents to be used for RAG
urls = ["chat.rst", "llama3.rst", "memory_optimizations.rst", "lora_finetune.rst"]
documents = [
    Document(
        document_id=f"num-{i}",
        content=f"https://raw.githubusercontent.com/pytorch/torchtune/main/docs/source/tutorials/{url}",
        mime_type="text/plain",
        metadata={},
    )
    for i, url in enumerate(urls)
]

# Register a database
vector_db_id = f"test-vector-db-{uuid.uuid4().hex}"
client.vector_dbs.register(
    vector_db_id=vector_db_id,
    embedding_model="all-MiniLM-L6-v2",
    embedding_dimension=384,
    extra_query={"search_mode": "keyword"},
)

# Insert the documents into the vector database
client.tool_runtime.rag_tool.insert(
    documents=documents,
    vector_db_id=vector_db_id,
    chunk_size_in_tokens=512,
)

print("************************** VECTOR ***************************************************")

query_config = RAGQueryConfig(max_chunks=6, search_mode="vector").model_dump()
results = client.tool_runtime.rag_tool.query(
    vector_db_ids=[vector_db_id], content="what is torchtune", query_config=query_config
)
print(results.to_json())

print("************************** KEYWORD ***************************************************")

query_config = RAGQueryConfig(max_chunks=6, search_mode="keyword").model_dump()
results = client.tool_runtime.rag_tool.query(
    vector_db_ids=[vector_db_id], content="what is torchtune", query_config=query_config
)
print(results.to_json())
