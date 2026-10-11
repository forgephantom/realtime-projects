# Architecture (HLD) — Semantic Similarity Evaluator: Vector_Db_Sim

## Problem & Users

Semantic Similarity Evaluator built as a vector_db_sim. Semantic similarity judges whether two texts mean the same thing, using embedding vectors and cosine similarity instead of word overlap. It rewards good paraphrases that n-gram metrics punish, but it needs a threshold calibrated on labeled pairs and it can miss subtle negation flips. The simulation builds sentence embeddings from seeded random projections to demonstrate the geometry. An in-memory vector database that stores vectors with metadata, runs cosine-similarity top-k search, and persists the index as JSON.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Semantic Similarity Evaluator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| VectorDB | main | In-memory vector store: add vectors with metadata, cosine top-k search, JSON save/load. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
vectors + metadata -> VectorDB.add -> in-memory index
query vector -> VectorDB.search (cosine top-k) -> ranked hits
index -> VectorDB.save -> JSON file -> VectorDB.load -> index
```

## Storage

The index persists as a single JSON file (vectors plus metadata); nothing else is stored.

## Scaling & Limits

Brute-force scan suits tens of thousands of vectors; millions would need an approximate index like HNSW.

## Trade-offs

Exact brute-force search is simple and correct but linear in index size, unlike approximate indexes.

## Failure Handling

Adding a vector with a different dimension than the index raises a clear error instead of silently corrupting search.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
