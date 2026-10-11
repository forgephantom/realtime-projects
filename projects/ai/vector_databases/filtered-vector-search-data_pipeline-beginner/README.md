# Filtered Vector Search: Data Pipeline (Etl)

**Domain:** ai | **Subdomain:** vector_databases | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Filtered Vector Search built as a Data pipeline (ETL). Filtered vector search applies metadata filters before or during similarity ranking, so results respect constraints like category or date range. Pre-filtering is exact but can starve the result set; post-filtering is approximate but flexible. The simulation compares both on selective filters. Extracts synthetic topic records, transforms them (drop invalid, normalize, bucket), and loads the clean set to CSV.

**Core concept — Filtered Vector Search:** Filtered vector search applies metadata filters before or during similarity ranking, so results respect constraints like category or date range. Pre-filtering is exact but can starve the result set; post-filtering is approximate but flexible. The simulation compares both on selective filters.

**Why this matters in the real world:** Catalog search restricts semantic results to in-stock or in-category items.

---

## Features

- **Pipeline**: Three-stage ETL pipeline for topic records.
- `generate_raw` (`generate_raw(seed, n)`): Extract stage: build synthetic raw records.
- `clean_rows` (`clean_rows(rows)`): Transform stage: drop invalid rows, normalize, bucket. Returns (clean_rows, dropped_count).
- `write_csv` (`write_csv(path, rows)`): Load stage: write rows to a CSV file.
- `Pipeline.extract` (`Pipeline.extract(self, n)`): Run the extract stage and return raw rows.
- `Pipeline.transform` (`Pipeline.transform(self, rows)`): Run the transform stage and return (clean, dropped).
- `Pipeline.load` (`Pipeline.load(self, rows)`): Run the load stage; return the CSV path written.
- `Pipeline.run` (`Pipeline.run(self, n)`): Run extract -> transform -> load; print a stage report.
- `main` (`main()`): Parse args and run the pipeline.

---

## Tech Stack

Python 3.8+, stdlib: argparse, csv, os, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Extract -> transform -> load over synthetic records. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) across all three stages. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/vector_databases/filtered-vector-search-data_pipeline-beginner
python3 src/main.py --help
python3 src/main.py
```
The pipeline writes demo_workspace/records_clean.csv in the current working directory; use --out-dir to change it.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A stage report table (extracted, dropped, loaded row counts), bucket distribution, five sample rows, and the CSV path.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
