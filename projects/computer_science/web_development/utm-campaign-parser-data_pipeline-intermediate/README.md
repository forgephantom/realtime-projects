# UTM Campaign Parser: Data Pipeline (Etl)

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

UTM Campaign Parser built as a Data pipeline (ETL). Marketing attribution starts with UTM tags: the parser extracts utm_source/medium/campaign from URLs, normalizes naming conventions, attributes sessions to campaigns, and reports spend efficiency per campaign. Consistent taxonomy is enforced because 'Email' vs 'email' splits reports. It is unglamorous and essential. Extracts synthetic topic records, transforms them (drop invalid, normalize, bucket), and loads the clean set to CSV.

**Core concept — UTM Campaign Parser:** Marketing attribution starts with UTM tags: the parser extracts utm_source/medium/campaign from URLs, normalizes naming conventions, attributes sessions to campaigns, and reports spend efficiency per campaign. Consistent taxonomy is enforced because 'Email' vs 'email' splits reports. It is unglamorous and essential.

**Why this matters in the real world:** Every marketing team (HubSpot, Marketo users) standardizes UTMs for campaign ROI reporting.

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
cd projects/computer_science/web_development/utm-campaign-parser-data_pipeline-intermediate
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
