# Design (LLD) — Sentence Window Retrieval: Rag_Simulator

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| chunk_documents | chunk_documents(documents: list, chunk_size: int = 40, overlap: int = 10) -> list | Split documents into fixed-size word chunks with overlap; returns chunk dicts. |
| score_chunk | score_chunk(chunk_tokens: list, query_terms: list, idf: dict) -> float | TF-IDF-style term-overlap score of one chunk for the query terms. |
| retrieve | retrieve(chunks: list, query: str, idf: dict, k: int = 3) -> list | Rank chunks by score_chunk and return the top-k with scores. |
| generate_answer | generate_answer(query: str, chunks: list, idf: dict, k: int = 2) -> dict | Return the top-ranked chunk as the answer plus a citation string. |
| run_demo | run_demo(seed: int, query: str = None) -> int | Seeded end-to-end demo: corpus, chunks, ranked hits, answer, citation. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded RAG pipeline demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Sentence Window Retrieval:

| Parameter | Meaning |
|---|---|
| embedding_unit | sentence-level embeddings |
| hits | sentences retrieved per query |
| window_size | neighboring sentences included |

## Algorithm & Complexity

The core of this project is Fixed-size word chunking with overlap, TF-IDF-weighted term-overlap retrieval, extractive answer from the top chunk with citation..

- **Time complexity:** O(C*T) to score C chunks against T query terms; IDF build is O(total tokens).
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/rag_systems/sentence-window-retrieval-rag_simulator-beginner
python3 src/main.py --help
python3 src/main.py
```
--query overrides the seeded demo query; chunk size and overlap come from the project params.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
