# Design (LLD) — SRS Section Builder: Report Generator

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
| generate_records | generate_records(n: int, rng: random.Random) -> list | Build n seeded synthetic measurement records for the demo. |
| summarize | summarize(records: list) -> dict | Aggregate totals, per-service rollups, error rate, and latency peaks. |
| render_markdown | render_markdown(title: str, summary: dict, records: list) -> str | Render the summary and sample rows as a Markdown document. |
| write_report | write_report(path: str, text: str) -> str | Write the Markdown report, creating parent folders; return the path. |
| run_demo | run_demo(seed: int, n_rows: int, out_path: str) -> int | Generate data, summarize it, write the report, print a summary. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the report demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for SRS Section Builder:

| Parameter | Meaning |
|---|---|
| features | system features specified |
| requirements | tagged requirements per feature |
| sections | SRS section templates |

## Algorithm & Complexity

The core of this project is Seeded synthetic data generation, aggregation rollups, Markdown rendering.

- **Time complexity:** O(n) to generate and summarize n records
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/business_analyst/requirements_management/srs-section-builder-report_generator-beginner
python3 src/main.py --help
python3 src/main.py
```
--rows sets the record count; --out sets the report path (default ./demo_output/report.md); --title sets the heading.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
