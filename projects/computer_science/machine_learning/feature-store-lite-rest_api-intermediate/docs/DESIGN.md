# Design (LLD) — Feature Store (Lite): Rest Api Service

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Store | In-memory record collection backing the API. |
| ApiHandler | BaseHTTPRequestHandler routing GET/POST to the Store. |

## Functions

| Function | Signature | Description |
|---|---|---|
| seed_records | seed_records(seed, count) | Generate deterministic synthetic records. |
| Store.list_records | Store.list_records(self) | Return a copy of all stored records. |
| Store.add_record | Store.add_record(self, payload) | Append a record built from the posted JSON payload. |
| Store.stats | Store.stats(self) | Aggregate record count, mean value, and active count. |
| start_server | start_server(port, seed, count) | Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread. |
| run_self_test | run_self_test(base_url, seed) | Exercise every endpoint with urllib and print a results table. |
| main | main() | Parse args; self-test by default or serve with --serve. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Feature Store (Lite):

| Parameter | Meaning |
|---|---|
| features | registered feature definitions |
| ttl | online store freshness |
| backfill | historical recompute policy |

## Algorithm & Complexity

The core of this project is In-memory CRUD over HTTP with JSON bodies.

- **Time complexity:** O(n) per list/stats request, O(1) per create
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/machine_learning/feature-store-lite-rest_api-intermediate
python3 src/main.py --help
python3 src/main.py
```
Add --serve to keep the server running instead of self-testing.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
