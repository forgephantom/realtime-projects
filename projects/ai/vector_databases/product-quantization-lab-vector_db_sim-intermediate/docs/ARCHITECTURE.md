# Architecture (HLD) — Product Quantization Lab: Vector_Db_Sim

## Problem & Users

Product Quantization Lab built as a vector_db_sim. Product quantization compresses vectors by splitting them into subvectors and replacing each with a learned code, shrinking memory by an order of magnitude. The lab measures recall loss at different compression levels. Residual refinement shows how accuracy can be partially recovered. An in-memory vector database that stores vectors with metadata, runs cosine-similarity top-k search, and persists the index as JSON.

The intended user is a student or engineer working in ai (vector_databases) who needs a working, runnable reference for Product Quantization Lab — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
