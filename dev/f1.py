import json
import re
import string
import uuid
from typing import Dict, List, Set

import matplotlib.pyplot as plt

from llama_stack_client.types import Document
from llama_stack.apis.tools import RAGQueryConfig


def create_library_client(template="ollama"):
    from llama_stack import LlamaStackAsLibraryClient
    client = LlamaStackAsLibraryClient(template)
    client.initialize()
    return client

client = create_library_client()


def normalize_answer(s): # taken from evaluation script
    if isinstance(s, list):
        s = " ".join(str(item) for item in s)
    elif not isinstance(s, str):
        s = str(s)

    def remove_articles(text): return re.sub(r"\b(a|an|the)\b", " ", text)
    def white_space_fix(text): return " ".join(text.split())
    def remove_punc(text): return "".join(ch for ch in text if ch not in string.punctuation)
    def lower(text): return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def compute_recall_metrics(gold_titles: Set[str], retrieved_titles: List[str]) -> Dict[str, float]:
    def hit_at_k(k):
        return 1.0 if any(title in gold_titles for title in retrieved_titles[:k]) else 0.0

    return {
        "Recall@1": hit_at_k(1),
        "Recall@3": hit_at_k(3),
        "Recall@5": hit_at_k(5),
    }

def compute_precision_metrics(gold_titles: Set[str], retrieved_titles: List[str]) -> Dict[str, float]:
    def precision_at_k(k):
        top_k = retrieved_titles[:k]
        if not top_k:
            return 0.0
        correct = sum(1 for title in top_k if title in gold_titles)
        return correct / k

    return {
        "Precision@1": precision_at_k(1),
        "Precision@3": precision_at_k(3),
        "Precision@5": precision_at_k(5),
    }

def compute_f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def load_hotpotqa(path, limit=50):
    with open(path) as f:
        data = json.load(f)
    qa_pairs = []
    documents = []
    for idx, item in enumerate(data[:limit]):
        question = item["question"]
        supporting_titles = {title for title, _ in item["supporting_facts"]}
        for title, text in item["context"]:
            doc_id = f"{idx}_{title.replace(' ', '_')}"
            text = " ".join(text).strip() if isinstance(text, list) else text.strip()
            documents.append(Document(document_id=doc_id, content=text, metadata={"title": title}))
        qa_pairs.append((question, supporting_titles))
    return qa_pairs, documents


def evaluate_retriever(chunk_size: int, embedding_dimension: int, limit: int):
    hotpot_path = "dev/hotpot_dev_distractor_v1.json"
    qa_pairs, documents = load_hotpotqa(hotpot_path, limit=limit)
    vector_db_id = f"hotpotqa-db-{uuid.uuid4().hex}"

    client.vector_dbs.register(
        vector_db_id=vector_db_id,
        embedding_model="all-MiniLM-L6-v2",
        embedding_dimension=embedding_dimension,
    )

    client.tool_runtime.rag_tool.insert(
        documents=documents,
        vector_db_id=vector_db_id,
        chunk_size_in_tokens=chunk_size,
    )

    recall_buckets = {"Recall@1": [], "Recall@3": [], "Recall@5": []}
    precision_buckets = {"Precision@1": [], "Precision@3": [], "Precision@5": []}
    doc_id_to_title = {doc.document_id: doc.metadata.get("title", "") for doc in documents}

    for idx, (question, supporting_titles) in enumerate(qa_pairs):
        query_config = RAGQueryConfig(max_chunks=5, search_mode="vector").model_dump()
        result = client.tool_runtime.rag_tool.query(
            vector_db_ids=[vector_db_id],
            content=question,
            query_config=query_config,
        )

        retrieved_ids = result.metadata.get("document_ids", [])
        retrieved_titles = [doc_id_to_title.get(doc_id, "") for doc_id in retrieved_ids]

        recall_scores = compute_recall_metrics(supporting_titles, retrieved_titles)
        precision_scores = compute_precision_metrics(supporting_titles, retrieved_titles)

        for key in recall_buckets.keys():
            recall_buckets[key].append(recall_scores[key])
        for key in precision_buckets.keys():
            precision_buckets[key].append(precision_scores[key])

    avg_recall = {key: sum(scores) / len(scores) for key, scores in recall_buckets.items()}
    avg_precision = {key: sum(scores) / len(scores) for key, scores in precision_buckets.items()}
    return avg_recall, avg_precision


def main():
    chunk_size = 256
    embedding_dim = 64
    limits = [50, 60, 70, 80]

    recall_results = {"Recall@1": [], "Recall@3": [], "Recall@5": []}
    precision_results = {"Precision@1": [], "Precision@3": [], "Precision@5": []}
    f1_results = {"F1@1": [], "F1@3": [], "F1@5": []}

    for limit in limits:
        print(f"Running for limit: {limit}")
        avg_recall, avg_precision = evaluate_retriever(chunk_size=chunk_size, embedding_dimension=embedding_dim, limit=limit)
        for key in recall_results:
            recall_results[key].append(avg_recall[key])
        for key in precision_results:
            precision_results[key].append(avg_precision[key])

        for k in ["1", "3", "5"]:
            prec = avg_precision[f"Precision@{k}"]
            rec = avg_recall[f"Recall@{k}"]
            f1 = compute_f1(prec, rec)
            f1_results[f"F1@{k}"].append(f1)

    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # Recall plot
    for key in recall_results:
        axes[0].plot(limits, recall_results[key], marker="o", label=key)
        for i, value in enumerate(recall_results[key]):
            axes[0].text(limits[i], value + 0.01, f"{limits[i]}", ha='center', fontsize=8)

    axes[0].set_xlabel("Dataset Size (limit)")
    axes[0].set_ylabel("Recall")
    axes[0].set_title("Recall@K vs Dataset Size\n(embedding_dim=64, chunk_size=256)")
    axes[0].legend()
    axes[0].grid(True)

    # Precision plot
    for key in precision_results:
        axes[1].plot(limits, precision_results[key], marker="o", label=key)
        for i, value in enumerate(precision_results[key]):
            axes[1].text(limits[i], value + 0.01, f"{limits[i]}", ha='center', fontsize=8)

    axes[1].set_xlabel("Dataset Size (limit)")
    axes[1].set_ylabel("Precision")
    axes[1].set_title("Precision@K vs Dataset Size\n(embedding_dim=64, chunk_size=256)")
    axes[1].legend()
    axes[1].grid(True)

    # F1 plot
    for key in f1_results:
        axes[2].plot(limits, f1_results[key], marker="o", label=key)
        for i, value in enumerate(f1_results[key]):
            axes[2].text(limits[i], value + 0.01, f"{limits[i]}", ha='center', fontsize=8)

    axes[2].set_xlabel("Dataset Size (limit)")
    axes[2].set_ylabel("F1 Score")
    axes[2].set_title("F1@K vs Dataset Size\n(embedding_dim=64, chunk_size=256)")
    axes[2].legend()
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
