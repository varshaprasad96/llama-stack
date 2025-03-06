import asyncio
import sqlite3
import inspect
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

query_params = inspect.signature(sqlite_vec_index.query).parameters
print("\n🔍 **Query API Supports the Following Parameters:**")
for param_name, param_details in query_params.items():
    print(f"  - {param_name} (Type: {param_details.annotation})")

# ✅ Step 3: Insert sample text chunks + embeddings
sample_chunks = [
    Chunk(content="Machine learning is transforming AI research.", metadata={"document_id": "doc-1"}),
    Chunk(content="Deep learning is a subset of machine learning.", metadata={"document_id": "doc-2"}),
    Chunk(content="Reinforcement learning helps train AI agents.", metadata={"document_id": "doc-3"}),
    Chunk(content="Vector search is useful for retrieving similar documents.", metadata={"document_id": "doc-4"}),
    Chunk(content="Neural networks are the backbone of deep learning.", metadata={"document_id": "doc-5"}),
]

# Generate random embeddings (replace with real embeddings in production)
np.random.seed(42)
sample_embeddings = np.array([np.random.rand(EMBEDDING_DIMENSION).astype(np.float32) for _ in sample_chunks])

# ✅ Insert the chunks into the vector DB
asyncio.run(sqlite_vec_index.add_chunks(sample_chunks, sample_embeddings))

# ✅ Function to perform Keyword-Based Search
async def keyword_search(query_str, top_k=3):
    print(f"\n🔍 Keyword Search for: '{query_str}'")
    response = await sqlite_vec_index.query(
        embedding=None, query_str=query_str, k=top_k, score_threshold=0.0, search_mode="keyword"
    )
    for chunk, score in zip(response.chunks, response.scores):
        print(f"📄 {chunk.metadata['document_id']}: {chunk.content} (Score: {score})")

# ✅ Function to perform Vector-Based Search
async def vector_search(query_embedding, top_k=3):
    print("\n🔍 Vector Search Results:")
    response = await sqlite_vec_index.query(
        embedding=query_embedding, query_str="", k=top_k, score_threshold=0.0, search_mode="vector"
    )
    for chunk, score in zip(response.chunks, response.scores):
        print(f"📄 {chunk.metadata['document_id']}: {chunk.content} (Score: {score:.4f})")

# ✅ Run Keyword Search
asyncio.run(keyword_search("deep learning"))

# ✅ Run Vector Search (Using a random vector as a query)
query_embedding = np.random.rand(EMBEDDING_DIMENSION).astype(np.float32)  # Replace with real embedding
asyncio.run(vector_search(query_embedding))

# Close connection
conn.close()
