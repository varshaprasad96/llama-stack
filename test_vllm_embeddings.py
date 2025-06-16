# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import asyncio
import base64
import logging
import struct

import httpx
from openai import AsyncOpenAI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def decode_base64_embedding(base64_str: str) -> list[float]:
    """Decode base64 string to list of floats."""
    # Decode base64 to bytes
    decoded_bytes = base64.b64decode(base64_str)

    # assuming 32-bit floats
    floats = []
    for i in range(0, len(decoded_bytes), 4):
        if i + 4 <= len(decoded_bytes):
            float_val = struct.unpack("f", decoded_bytes[i : i + 4])[0]
            floats.append(float_val)

    return floats


async def test_embeddings():
    # Initialize the client with the server URL
    client = AsyncOpenAI(
        base_url="http://vllm-llamastack.apps.rosa.ibaranau.g9ax.p3.openshiftapps.com/v1",
        api_key="dummy-key",  # vLLM doesn't require authentication, required as this is failing otherwise.
        http_client=httpx.AsyncClient(verify=False),  # Disable SSL verification for testing
    )

    # Test inputs
    test_inputs = ["The quick brown fox jumps over the lazy dog", "A fast orange fox leaps over a sleepy canine"]

    # Test with float encoding
    logger.info("Testing with float encoding...")
    float_response = await client.embeddings.create(
        model="intfloat/e5-small-v2", input=test_inputs, encoding_format="float"
    )
    logger.info(f"Raw float_response: {float_response}")
    logger.info(f"Raw float_response JSON: {getattr(float_response, 'model_dump_json', lambda: str(float_response))()}")
    if float_response.data is None:
        logger.error("float_response.data is None!")
        return
    logger.info(f"Float embeddings shape: {len(float_response.data[0].embedding)}")
    logger.info(f"First few values of first embedding: {float_response.data[0].embedding[:5]}")

    # Test with base64 encoding
    logger.info("\nTesting with base64 encoding...")
    base64_response = await client.embeddings.create(
        model="intfloat/e5-small-v2", input=test_inputs, encoding_format="base64"
    )
    logger.info(f"Raw base64_response: {base64_response}")
    logger.info(
        f"Raw base64_response JSON: {getattr(base64_response, 'model_dump_json', lambda: str(base64_response))()}"
    )
    if base64_response.data is None:
        logger.error("base64_response.data is None!")
        return

    # Decode base64 embeddings
    float_embeddings = [data.embedding for data in float_response.data]
    base64_embeddings = []
    for data in base64_response.data:
        try:
            # Decode base64 string to float list
            decoded_floats = decode_base64_embedding(data.embedding)
            base64_embeddings.append(decoded_floats)
        except Exception as e:
            logger.error(f"Error decoding base64 embedding: {e}")
            return

    # Compare embeddings
    logger.info("\nComparing embeddings:")
    logger.info(f"Number of float embeddings: {len(float_embeddings)}")
    logger.info(f"Number of base64 embeddings: {len(base64_embeddings)}")

    if len(float_embeddings) == len(base64_embeddings):
        for i, (float_emb, base64_emb) in enumerate(zip(float_embeddings, base64_embeddings, strict=False)):
            logger.info(f"\nEmbedding {i}:")
            logger.info(f"Float embedding length: {len(float_emb)}")
            logger.info(f"Base64 embedding length: {len(base64_emb)}")
            logger.info(f"First few values of float embedding: {float_emb[:5]}")
            logger.info(f"First few values of base64 embedding: {base64_emb[:5]}")

            # Check if the embeddings are similar
            if len(float_emb) == len(base64_emb):
                # Calculate mean absolute difference
                mean_diff = sum(abs(f - b) for f, b in zip(float_emb, base64_emb, strict=False)) / len(float_emb)
                logger.info(f"Mean absolute difference between float and base64 embeddings: {mean_diff}")
            else:
                logger.error("Embedding lengths don't match!")
    else:
        logger.error("Mismatch in number of embeddings!")


if __name__ == "__main__":
    asyncio.run(test_embeddings())
