# Architecture (HLD) — Long Context Evaluator: Rag_Simulator

## Problem & Users

Long Context Evaluator built as a rag_simulator. Long-context models are tested with needle-in-a-haystack retrieval: a fact is buried at varying depths in a long document and the model must find it. Performance typically degrades near the middle of the context, the lost-in-the-middle effect. The evaluator sweeps context length and needle depth to map the retrieval frontier. A retrieval-augmented generation pipeline simulator that chunks documents, retrieves passages with TF-IDF-style scoring, and answers extractively with citations.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Long Context Evaluator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
