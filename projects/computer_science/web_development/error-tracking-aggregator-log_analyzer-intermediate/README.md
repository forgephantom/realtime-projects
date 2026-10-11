# Error Tracking Aggregator: Log Analyzer

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Error Tracking Aggregator built as a Log analyzer. Raw exceptions are noise until grouped: the aggregator fingerprints stack traces (normalizing line numbers and memory addresses), counts occurrences per issue, and tracks first-seen, regression, and release correlation. Grouping quality decides whether developers see ten real bugs or ten thousand duplicates. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — Error Tracking Aggregator:** Raw exceptions are noise until grouped: the aggregator fingerprints stack traces (normalizing line numbers and memory addresses), counts occurrences per issue, and tracks first-seen, regression, and release correlation. Grouping quality decides whether developers see ten real bugs or ten thousand duplicates.

**Why this matters in the real world:** Sentry, Rollbar, and Bugsnag fingerprint and group errors exactly this way.

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
cd projects/computer_science/web_development/error-tracking-aggregator-log_analyzer-intermediate
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
