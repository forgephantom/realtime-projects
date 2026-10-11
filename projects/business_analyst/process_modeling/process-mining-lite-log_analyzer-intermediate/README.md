# Process Mining Lite: Log Analyzer

**Domain:** business_analyst | **Subdomain:** process_modeling | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Process Mining Lite built as a Log analyzer. Process mining reconstructs the real process from event logs: which paths cases actually took, where they looped, and how long each variant lasted. The discovered model almost always differs from the documented one. The lite version builds the variant map and conformance gaps from seeded logs. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — Process Mining Lite:** Process mining reconstructs the real process from event logs: which paths cases actually took, where they looped, and how long each variant lasted. The discovered model almost always differs from the documented one. The lite version builds the variant map and conformance gaps from seeded logs.

**Why this matters in the real world:** Enterprises mine ERP logs to find how purchasing really happens versus policy.

---

## Features

- `generate_log` (`generate_log(seed, lines)`): Generate synthetic topic log lines in memory.
- `parse_line` (`parse_line(line)`): Parse one log line; return a dict or None if unparseable.
- `analyze` (`analyze(entries)`): Aggregate level counts, service counts, and top error messages.
- `print_report` (`print_report(report, total)`): Print the analysis report.
- `main` (`main()`): Parse args, generate, parse, and report.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, re, collections, datetime

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Regex parsing with Counter aggregation. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) to generate, parse, and aggregate n lines. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/process_modeling/process-mining-lite-log_analyzer-intermediate
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Level counts with percentages, service counts, the error rate, and the top five error messages with counts.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
