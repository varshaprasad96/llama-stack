# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from uuid import uuid4

import fire
from llama_stack_client import LlamaStackClient, RAGDocument
from termcolor import colored


def run_main(host: str, port: int, user_prompt: str = None, disable_safety: bool = False):
    urls = [
        "memory_optimizations.rst",
        "chat.rst",
        "llama3.rst",
        "datasets.rst",
        "qat_finetune.rst",
        "lora_finetune.rst",
    ]
    documents = [
        RAGDocument(
            document_id=f"num-{i}",
            content=f"https://raw.githubusercontent.com/pytorch/torchtune/main/docs/source/tutorials/{url}",
            mime_type="text/plain",
            metadata={},
        )
        for i, url in enumerate(urls)
    ]
    client = LlamaStackClient(base_url=f"http://{host}:{port}")

    vector_providers = [provider for provider in client.providers.list() if provider.api == "vector_io"]

    print("***********", vector_providers)
    if not vector_providers:
        print(colored("No available vector_io providers. Exiting.", "red"))
        return

    selected_vector_provider = vector_providers[0]

    # Create a vector database instead of memory bank
    vector_db_id = f"test_vector_db_{uuid4()}"
    client.vector_dbs.register(
        vector_db_id=vector_db_id,
        embedding_model="all-MiniLM-L6-v2",
        embedding_dimension=384,
        provider_id=selected_vector_provider.provider_id,
    )

    # Insert documents using the RAG tool
    client.tool_runtime.rag_tool.insert(
        documents=documents,
        vector_db_id=vector_db_id,
        chunk_size_in_tokens=512,
    )

    print("successfully inserted documents into vector db")

    # Get available LLM models
    available_models = client.models.list()
    available_models = [model.identifier for model in available_models if model.model_type == "llm"]

    if not available_models:
        print(colored("No available LLM models. Exiting.", "red"))
        return

    selected_model = available_models[0]
    print(f"Using model: {selected_model}")

    # Use provided user prompt or default
    if user_prompt is None:
        user_prompt = "What are the main topics covered in the documentation?"

    print(f"\n{'=' * 50}")
    print(f"User Query: {user_prompt}")
    print(f"{'=' * 50}")

    # Query the vector DB to get relevant context
    rag_response = client.tool_runtime.rag_tool.query(content=user_prompt, vector_db_ids=[vector_db_id])

    # Extract text content from the response
    prompt_context = ""
    if hasattr(rag_response.content, "__iter__"):
        for item in rag_response.content:
            if hasattr(item, "text"):
                prompt_context += item.text
    else:
        prompt_context = str(rag_response.content)

    print("\nRetrieved Context:")
    print(f"{'-' * 30}")
    print(prompt_context)
    print(f"{'-' * 30}")

    # Construct the extended prompt with context
    system_prompt = """You are a helpful assistant that answers questions based on the provided context. 
Follow these guidelines:
1. Only use information from the provided context
2. If the context doesn't contain relevant information, say so
3. Be concise and accurate
4. Cite specific parts of the context when possible"""

    extended_prompt = f"Please answer the following query using the context below.\n\nCONTEXT:\n{prompt_context}\n\nQUERY:\n{user_prompt}"

    # Prepare messages for inference
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": extended_prompt}]

    # Run inference directly
    print("\nGenerating response...")
    response = client.inference.chat_completion(
        messages=messages,
        model_id=selected_model,
        sampling_params={
            "strategy": {"type": "greedy"},
        },
        stream=False,  # Set to False for simpler output
    )

    # Display the response
    print("\nResponse:")
    print(f"{'-' * 30}")
    print(response.completion_message.content)
    print(f"{'-' * 30}")


def main(host: str, port: int, prompt: str = None):
    run_main(host, port, prompt)


if __name__ == "__main__":
    fire.Fire(main)
