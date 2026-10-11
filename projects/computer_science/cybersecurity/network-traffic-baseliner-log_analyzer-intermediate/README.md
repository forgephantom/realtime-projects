# Network Traffic Baseliner: Log Analyzer

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Network Traffic Baseliner built as a Log analyzer. You cannot spot abnormal traffic without knowing what normal looks like, so a baseliner records bytes, flows, ports, and peer counts per host over time. It stores hourly profiles and compares live traffic against them with simple statistical distance, producing a ranked list of the most deviant hosts. Analysts start investigations from the top of that list. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — Network Traffic Baseliner:** You cannot spot abnormal traffic without knowing what normal looks like, so a baseliner records bytes, flows, ports, and peer counts per host over time. It stores hourly profiles and compares live traffic against them with simple statistical distance, producing a ranked list of the most deviant hosts. Analysts start investigations from the top of that list.

**Why this matters in the real world:** Used by NOC and SOC teams as the first pass of network anomaly hunting.

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
cd projects/computer_science/cybersecurity/network-traffic-baseliner-log_analyzer-intermediate
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
