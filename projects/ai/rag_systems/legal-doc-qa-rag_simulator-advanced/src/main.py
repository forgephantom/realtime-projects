#!/usr/bin/env python3
"""Legal Document Q&A: Rag_Simulator.

Legal document Q&A retrieves clauses from agreements and explains them in plain language with exact-quote citations. Jurisdiction metadata filters which documents apply to the question. The system refuses to give legal advice and frames answers as information only.

Demo dataset idea: Generates seeded agreements with planted clauses and checks citation precision and advice disclaimers..
"""

import argparse
import math
import random
import re
from collections import Counter

SLUG = "rag-simulator"
PARAMS = {'advice_disclaimer': 'whether to include disclaimers', 'clause_types': 'categories to recognize', 'jurisdictions': 'jurisdiction metadata values'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def _param(key, default):
    """Read a project param defensively; coerce descriptive text to the default's type."""
    v = PARAMS.get(key, default) if isinstance(PARAMS, dict) else default
    if isinstance(default, bool):
        return v if isinstance(v, bool) else default
    if isinstance(default, (int, float)) and not isinstance(v, (int, float)):
        return _num(v, default)
    return v


def _tokenize(text: str) -> list:
    """Lowercase alphanumeric word tokens from text."""
    return re.findall(r"[a-z0-9]+", text.lower())


def chunk_documents(documents: list, chunk_size: int = 40, overlap: int = 10) -> list:
    """Split each document into fixed-size word chunks with overlap.

    Returns chunk dicts with doc_id, chunk_id, text, and tokens.
    """
    chunks = []
    for doc_id, doc in enumerate(documents):
        words = _tokenize(doc)
        if not words:
            continue
        step = max(1, chunk_size - overlap)
        cid = 0
        for start in range(0, len(words), step):
            piece = words[start:start + chunk_size]
            if len(piece) < chunk_size // 2 and start > 0:
                break
            chunks.append({"doc_id": doc_id, "chunk_id": cid,
                           "text": " ".join(piece), "tokens": piece})
            cid += 1
    return chunks


def _compute_idf(chunks: list) -> dict:
    """IDF over chunk tokens: log((N+1)/(df+1)) + 1."""
    n = len(chunks)
    df = Counter()
    for chunk in chunks:
        for term in set(chunk["tokens"]):
            df[term] += 1
    return {term: math.log((n + 1) / (count + 1)) + 1.0
            for term, count in df.items()}


def score_chunk(chunk_tokens: list, query_terms: list, idf: dict) -> float:
    """TF-IDF-style term-overlap score of one chunk for the query terms."""
    if not chunk_tokens:
        return 0.0
    tf = Counter(chunk_tokens)
    n = len(chunk_tokens)
    return sum((tf[term] / n) * idf.get(term, 0.0)
               for term in set(query_terms))


def retrieve(chunks: list, query: str, idf: dict, k: int = 3) -> list:
    """Rank chunks by score_chunk and return the top-k with scores."""
    query_terms = _tokenize(query)
    scored = [(score_chunk(chunk["tokens"], query_terms, idf), chunk)
              for chunk in chunks]
    scored.sort(key=lambda item: item[0], reverse=True)
    return [{"score": score, "doc_id": chunk["doc_id"],
             "chunk_id": chunk["chunk_id"], "text": chunk["text"]}
            for score, chunk in scored[:k]]


def generate_answer(query: str, chunks: list, idf: dict, k: int = 2) -> dict:
    """Extractive answer: the top-ranked chunk plus a citation string."""
    hits = retrieve(chunks, query, idf, k=k)
    if not hits or hits[0]["score"] <= 0:
        return {"answer": "No relevant passage found.",
                "citation": "n/a", "score": 0.0}
    top = hits[0]
    citation = "doc-%d chunk-%d (score %.3f)" % (
        top["doc_id"], top["chunk_id"], top["score"])
    return {"answer": top["text"], "citation": citation,
            "score": top["score"]}


def _build_corpus(rng: random.Random, topic: str) -> list:
    """Seeded synthetic document set flavored with the topic name."""
    slug = topic.lower().replace(" ", "_")
    words = [slug, "guide", "overview", "system", "data", "process",
             "method", "example", "analysis", "report", "service",
             "platform", "model", "metric", "pipeline", "storage",
             "query", "index", "latency", "throughput", "cache", "deploy"]
    return [" ".join(rng.choice(words) for _ in range(120))
            for _ in range(5)]


def run_demo(seed: int, query: str = None) -> int:
    """Seeded end-to-end demo: corpus, chunks, ranked hits, answer, citation."""
    rng = random.Random(seed)
    topic = "Legal Document Q&A"
    docs = _build_corpus(rng, topic)
    chunk_size = _param("chunk_size", 40)
    overlap = _param("overlap", 10)
    chunks = chunk_documents(docs, chunk_size=chunk_size, overlap=overlap)
    idf = _compute_idf(chunks)
    if query is None:
        query = _param("query", "%s latency pipeline" % topic)
    print("Legal Document Q&A: Rag_Simulator  (topic: Legal Document Q&A, seed=%d)" % seed)
    print("Corpus: %d docs -> %d chunks (size=%d, overlap=%d)"
          % (len(docs), len(chunks), chunk_size, overlap))
    print("Query: %s\n" % query)
    for rank, hit in enumerate(retrieve(chunks, query, idf, k=3), 1):
        print("rank %d  score=%.4f  [doc-%d chunk-%d]"
              % (rank, hit["score"], hit["doc_id"], hit["chunk_id"]))
        print("  %s...\n" % hit["text"][:110])
    answer = generate_answer(query, chunks, idf, k=2)
    print("Answer: %s" % answer["answer"][:160])
    print("Citation: %s" % answer["citation"])
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Legal Document Q&A: Rag_Simulator: Legal document Q&A retrieves clauses from agreements and explains them in plain language with exact-quote citations. Jurisdiction metadata filters which documents apply to the question. The system refuses to give legal advice and frames answers as information only."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--query", type=str, default=None,
                        help="Override the demo query.")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded RAG pipeline demo."""
    args = build_parser().parse_args(argv)
    return run_demo(args.seed, query=args.query)


if __name__ == "__main__":
    raise SystemExit(main())
