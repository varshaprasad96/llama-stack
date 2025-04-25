# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
import os
import re
import string
import uuid
from collections import Counter
from typing import Dict, List, Set

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


client = create_library_client()


def normalize_answer(s):
    if isinstance(s, list):
        s = " ".join(str(item) for item in s)
    elif not isinstance(s, str):
        s = str(s)

    def remove_articles(text):
        return re.sub(r"\b(a|an|the)\b", " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        return "".join(ch for ch in text if ch not in string.punctuation)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def compute_recall_metrics(gold_titles: Set[str], retrieved_titles: List[str]) -> Dict[str, float]:
    def hit_at_k(k):
        return 1.0 if any(title in gold_titles for title in retrieved_titles[:k]) else 0.0

    return {
        "Recall@1": hit_at_k(1),
        "Recall@3": hit_at_k(3),
        "Recall@5": hit_at_k(5),
    }


def f1_score(prediction, ground_truth):
    pred_tokens = normalize_answer(prediction).split()
    truth_tokens = normalize_answer(ground_truth).split()
    common = Counter(pred_tokens) & Counter(truth_tokens)
    num_same = sum(common.values())
    if len(pred_tokens) == 0 or len(truth_tokens) == 0:
        return int(pred_tokens == truth_tokens)
    if num_same == 0:
        return 0
    precision = num_same / len(pred_tokens)
    recall = num_same / len(truth_tokens)
    return (2 * precision * recall) / (precision + recall)


def exact_match_score(prediction, ground_truth):
    return int(normalize_answer(prediction) == normalize_answer(ground_truth))


# ------------ Load HotpotQA ------------ #


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


def compute_recall_at_k(gold_titles: Set[str], retrieved_titles: list, k: int) -> float:
    top_k = retrieved_titles[:k]
    return 1.0 if any(title in gold_titles for title in top_k) else 0.0


# ------------ Main Evaluation ------------ #


def main():
    hotpot_path = "dev/hotpot_dev_distractor_v1.json"  # <-- update path if needed
    qa_pairs, documents = load_hotpotqa(hotpot_path, limit=50)
    vector_db_id = f"hotpotqa-db-{uuid.uuid4().hex}"

    client.vector_dbs.register(
        vector_db_id=vector_db_id,
        embedding_model="all-MiniLM-L6-v2",
        # embedding_dimension=384,
        embedding_dimension=384,
    )
    print(f" Registered Vector DB: {vector_db_id}")

    client.tool_runtime.rag_tool.insert(
        documents=documents,
        vector_db_id=vector_db_id,
        chunk_size_in_tokens=256,
    )
    print(f" Inserted {len(documents)} documents into vector DB")

    recalls = []
    recall_buckets = {"Recall@1": [], "Recall@3": [], "Recall@5": []}
    for idx, (question, supporting_titles) in enumerate(qa_pairs):
        query_config = RAGQueryConfig(max_chunks=5, search_mode="vector").model_dump()
        result = client.tool_runtime.rag_tool.query(
            vector_db_ids=[vector_db_id],
            content=question,
            query_config=query_config,
        )

        print("*************************")
        print(result)
        print("*************************")
        # Extract retrieved titles from metadata
        doc_id_to_title = {doc.document_id: doc.metadata.get("title", "") for doc in documents}

        retrieved_ids = result.metadata.get("document_ids", [])
        retrieved_titles = [doc_id_to_title.get(doc_id, "") for doc_id in retrieved_ids]

        # recall = compute_recall_at_k(supporting_titles, retrieved_titles, k=1)
        # recalls.append(recall)
        recall_scores = compute_recall_metrics(supporting_titles, retrieved_titles)
        for key, score in recall_scores.items():
            recall_buckets[key].append(score)
        print(f"Q: {question}")
        print(f"Supporting: {sorted(supporting_titles)}")
        print(f"Retrieved: {sorted(retrieved_titles[:5])}")
        print()

        # print(f"{idx + 1:02d} | Recall@5: {recall:.1f} | Q: {question}")

    # avg_recall = sum(recalls) / len(recalls)
    #
    # print(f"\n======================")
    # print(f" Average Recall@5: {avg_recall:.4f}")
    # print(f"======================")

    print("\n======================")
    for key, scores in recall_buckets.items():
        print(f" Average {key}: {sum(scores) / len(scores):.4f}")
    print("======================")
    # f1_scores, em_scores = [], []
    #
    # for idx, (question, ground_truth) in enumerate(qa_pairs):
    #     query_config = RAGQueryConfig(max_chunks=3, search_mode="vector").model_dump()
    #
    #     result = client.tool_runtime.rag_tool.query(
    #         vector_db_ids=[vector_db_id],
    #         content=question,
    #         query_config=query_config,
    #     )
    #
    #     pred = result.content if hasattr(result, "content") else str(result)
    #     f1 = f1_score(pred, ground_truth)
    #     em = exact_match_score(pred, ground_truth)
    #
    #     f1_scores.append(f1)
    #     em_scores.append(em)
    #
    #     print(f"{idx + 1:03} | F1: {f1:.2f} | EM: {em} | Q: {question} | Pred: {pred} | GT: {ground_truth}")
    #
    # avg_f1 = sum(f1_scores) / len(f1_scores)
    # avg_em = sum(em_scores) / len(em_scores)
    #
    # print("\n======================")
    # print(f"Average F1: {avg_f1:.4f}")
    # print(f"Average EM: {avg_em:.4f}")
    # print("======================")


if __name__ == "__main__":
    main()
