# Design (LLD) — Semantic Similarity Evaluator: Vector_Db_Sim

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| VectorDB | In-memory vector store: add vectors with metadata, cosine top-k search, JSON save/load. |

## Functions

| Function | Signature | Description |
|---|---|---|
| VectorDB.add | add(self, vector: list, metadata: dict = None) -> int | Store a vector with optional metadata; returns its integer id. |
| VectorDB.search | search(self, query: list, k: int = 5) -> list | Top-k cosine-similarity search; returns [{id, score, metadata}]. |
| VectorDB.save | save(self, path: str) -> None | Persist the index to a JSON file. |
| VectorDB.load | load(cls, path: str) -> "VectorDB" | Load an index previously written by save(). |
| run_demo | run_demo(seed: int) -> int | Seeded demo: clustered vectors, top-5 search, save/load roundtrip check. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded vector database demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Semantic Similarity Evaluator:

| Parameter | Meaning |
|---|---|
| embedding_dim | vector dimensionality |
| num_pairs | sentence pairs evaluated |
| threshold | similarity cutoff for equivalence |

## Algorithm & Complexity

The core of this project is Brute-force cosine similarity over stored vectors with a JSON-serialized index for save/load..

- **Time complexity:** O(N*D) per search over N vectors of dimension D; add is O(D).
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/model_evaluation/semantic-similarity-eval-vector_db_sim-intermediate
python3 src/main.py --help
python3 src/main.py
```
Vector dimension, count, and the index file path come from the project params.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
