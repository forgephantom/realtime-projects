# Multi-Hop Question Answering: Rag_Simulator

**Domain:** ai | **Subdomain:** rag_systems | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Multi-Hop Question Answering built as a rag_simulator. Multi-hop question answering chains multiple retrieval rounds, where each round's findings shape the next query. Bridge questions require combining facts from separate documents that share an entity. The simulation tracks hop accuracy and where chains break. A retrieval-augmented generation pipeline simulator that chunks documents, retrieves passages with TF-IDF-style scoring, and answers extractively with citations.

**Core concept — Multi-Hop Question Answering:** Multi-hop question answering chains multiple retrieval rounds, where each round's findings shape the next query. Bridge questions require combining facts from separate documents that share an entity. The simulation tracks hop accuracy and where chains break.

**Why this matters in the real world:** Analyst tools answer questions that span multiple reports and sources.

---

## Features

- `chunk_documents` (`chunk_documents(documents: list, chunk_size: int = 40, overlap: int = 10) -> list`): Split documents into fixed-size word chunks with overlap; returns chunk dicts.
- `score_chunk` (`score_chunk(chunk_tokens: list, query_terms: list, idf: dict) -> float`): TF-IDF-style term-overlap score of one chunk for the query terms.
- `retrieve` (`retrieve(chunks: list, query: str, idf: dict, k: int = 3) -> list`): Rank chunks by score_chunk and return the top-k with scores.
- `generate_answer` (`generate_answer(query: str, chunks: list, idf: dict, k: int = 2) -> dict`): Return the top-ranked chunk as the answer plus a citation string.
- `run_demo` (`run_demo(seed: int, query: str = None) -> int`): Seeded end-to-end demo: corpus, chunks, ranked hits, answer, citation.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded RAG pipeline demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, math, re, collections

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Fixed-size word chunking with overlap, TF-IDF-weighted term-overlap retrieval, extractive answer from the top chunk with citation.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(C*T) to score C chunks against T query terms; IDF build is O(total tokens).. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/rag_systems/multi-hop-qa-rag_simulator-advanced
python3 src/main.py --help
python3 src/main.py
```
--query overrides the seeded demo query; chunk size and overlap come from the project params.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints chunk counts, the top-3 ranked passages with scores, and the extractive answer with its citation.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
