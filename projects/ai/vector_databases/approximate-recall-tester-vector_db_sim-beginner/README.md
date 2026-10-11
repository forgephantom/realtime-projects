# Approximate Recall Tester: Vector_Db_Sim

**Domain:** ai | **Subdomain:** vector_databases | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Approximate Recall Tester built as a vector_db_sim. An approximate recall tester estimates true recall of an ANN index by comparing against brute-force ground truth on a sample of queries. Sampling strategy balances measurement cost against estimate confidence. The tester reports recall with confidence intervals. An in-memory vector database that stores vectors with metadata, runs cosine-similarity top-k search, and persists the index as JSON.

**Core concept — Approximate Recall Tester:** An approximate recall tester estimates true recall of an ANN index by comparing against brute-force ground truth on a sample of queries. Sampling strategy balances measurement cost against estimate confidence. The tester reports recall with confidence intervals.

**Why this matters in the real world:** Search quality teams monitor ANN index accuracy in production.

---

## Features

- **VectorDB**: In-memory vector store: add vectors with metadata, cosine top-k search, JSON save/load.
- `VectorDB.add` (`add(self, vector: list, metadata: dict = None) -> int`): Store a vector with optional metadata; returns its integer id.
- `VectorDB.search` (`search(self, query: list, k: int = 5) -> list`): Top-k cosine-similarity search; returns [{id, score, metadata}].
- `VectorDB.save` (`save(self, path: str) -> None`): Persist the index to a JSON file.
- `VectorDB.load` (`load(cls, path: str) -> "VectorDB"`): Load an index previously written by save().
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: clustered vectors, top-5 search, save/load roundtrip check.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded vector database demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, math, json

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Brute-force cosine similarity over stored vectors with a JSON-serialized index for save/load.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(N*D) per search over N vectors of dimension D; add is O(D).. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/vector_databases/approximate-recall-tester-vector_db_sim-beginner
python3 src/main.py --help
python3 src/main.py
```
Vector dimension, count, and the index file path come from the project params.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints the top-5 search hits with cosine scores and metadata, plus a save/load roundtrip verification line.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
