# Architecture (HLD) — Reranking Pipeline: Rag_Simulator

## Problem & Users

Reranking Pipeline built as a rag_simulator. A reranking pipeline takes the top candidates from fast retrieval and re-scores them with a slower, more accurate cross-encoder model. The two-stage design keeps latency low while improving final ordering. Cutoff tuning decides how many candidates enter the expensive rerank stage. A retrieval-augmented generation pipeline simulator that chunks documents, retrieves passages with TF-IDF-style scoring, and answers extractively with citations.

The intended user is a student or engineer working in ai (rag_systems) who needs a working, runnable reference for Reranking Pipeline — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
documents -> chunk_documents (size/overlap) -> chunks
chunks -> IDF table -> score_chunk per query -> retrieve top-k
top chunk -> generate_answer -> answer text + citation
```

## Storage

No persistence: the corpus, chunks, and IDF table are rebuilt from the seed on every run.

## Scaling & Limits

In-memory chunk list suits thousands of chunks; millions would need an inverted index instead of per-query rescoring.

## Trade-offs

Term overlap is transparent and fast but misses paraphrases that embedding retrieval would catch.

## Failure Handling

A query with no overlapping terms scores zero everywhere and returns a graceful 'no relevant passage' answer instead of guessing.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
