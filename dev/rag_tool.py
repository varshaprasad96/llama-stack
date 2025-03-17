# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from uuid import uuid4

import fire
from llama_stack_client import LlamaStackClient
from llama_stack_client.types import Document
from termcolor import colored


def run_main(host: str, port: int, disable_safety: bool = False):
    urls = [
        "memory_optimizations.rst",
        "chat.rst",
        "llama3.rst",
        "datasets.rst",
        "qat_finetune.rst",
        "lora_finetune.rst",
    ]
    documents = [
        Document(
            document_id=f"num-{i}",
            content=f"https://raw.githubusercontent.com/pytorch/torchtune/main/docs/source/tutorials/{url}",
            mime_type="text/plain",
            metadata={},
        )
        for i, url in enumerate(urls)
    ]

    client = LlamaStackClient(base_url="http://localhost:8321")

    vector_providers = [provider for provider in client.providers.list() if provider.api == "vector_io"]
    if not vector_providers:
        print(colored("No available vector_io providers. Exiting.", "red"))
        return

    selected_vector_provider = vector_providers[0]
    available_shields = [shield.identifier for shield in client.shields.list()]
    if not available_shields:
        print(colored("No available shields. Disabling safety.", "yellow"))
    else:
        print(f"Available shields found: {available_shields}")

    # Create a vector database instead of memory bank
    print("vector_db_id******")
    vector_db_id = f"test_vector_db_{uuid4()}"
    print(vector_db_id)
    client.vector_dbs.register(
        vector_db_id=vector_db_id,
        embedding_model="all-minilm:latest",
        embedding_dimension=384,
        provider_id=selected_vector_provider.provider_id,
    )

    # Insert documents using the RAG tool
    client.tool_runtime.rag_tool.insert(
        documents=documents,
        vector_db_id=vector_db_id,
        chunk_size_in_tokens=512,
    )


def main(host: str, port: int):
    run_main(host, port)


if __name__ == "__main__":
    fire.Fire(main)
