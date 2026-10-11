# Email Header Forensic Analyzer: Log Analyzer

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Email Header Forensic Analyzer built as a Log analyzer. Phishing emails betray themselves in their headers: mismatched from and return-path, failed SPF and DKIM, suspicious received chains, and odd reply-to addresses. The analyzer parses full headers, checks authentication results, traces the relay path, and scores the message for spoofing. It gives analysts a structured verdict instead of raw header soup. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — Email Header Forensic Analyzer:** Phishing emails betray themselves in their headers: mismatched from and return-path, failed SPF and DKIM, suspicious received chains, and odd reply-to addresses. The analyzer parses full headers, checks authentication results, traces the relay path, and scores the message for spoofing. It gives analysts a structured verdict instead of raw header soup.

**Why this matters in the real world:** Used by SOC analysts triaging reported phishing emails.

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
cd projects/computer_science/cybersecurity/email-header-forensic-analyzer-log_analyzer-beginner
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
