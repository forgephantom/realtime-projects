# Design (LLD) — Data Contract Checker: Data Pipeline (Etl)

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Pipeline | Three-stage ETL pipeline for topic records. |

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_raw | generate_raw(seed, n) | Extract stage: build synthetic raw records. |
| clean_rows | clean_rows(rows) | Transform stage: drop invalid rows, normalize, bucket. Returns (clean_rows, dropped_count). |
| write_csv | write_csv(path, rows) | Load stage: write rows to a CSV file. |
| Pipeline.extract | Pipeline.extract(self, n) | Run the extract stage and return raw rows. |
| Pipeline.transform | Pipeline.transform(self, rows) | Run the transform stage and return (clean, dropped). |
| Pipeline.load | Pipeline.load(self, rows) | Run the load stage; return the CSV path written. |
| Pipeline.run | Pipeline.run(self, n) | Run extract -> transform -> load; print a stage report. |
| main | main() | Parse args and run the pipeline. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Data Contract Checker:

| Parameter | Meaning |
|---|---|
| contracts | promises per dataset |
| deliveries | actual batches |
| slas | freshness and quality |
| breach | alerting |

## Algorithm & Complexity

The core of this project is Extract -> transform -> load over synthetic records.

- **Time complexity:** O(n) across all three stages
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/data_engineering/data-contract-checker-data_pipeline-intermediate
python3 src/main.py --help
python3 src/main.py
```
The pipeline writes demo_workspace/records_clean.csv in the current working directory; use --out-dir to change it.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
