# DNS Tunneling Detector: Log Analyzer

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

DNS Tunneling Detector built as a Log analyzer. DNS tunneling smuggles data out of a network by encoding it in subdomain labels of DNS queries, abusing a protocol that firewalls almost always allow. The detector scores queries on label entropy, query length, request frequency, and the rarity of the queried domain, because tunneled traffic looks random and chatty compared with human browsing. High-scoring domains get quarantined for analyst review. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — DNS Tunneling Detector:** DNS tunneling smuggles data out of a network by encoding it in subdomain labels of DNS queries, abusing a protocol that firewalls almost always allow. The detector scores queries on label entropy, query length, request frequency, and the rarity of the queried domain, because tunneled traffic looks random and chatty compared with human browsing. High-scoring domains get quarantined for analyst review.

**Why this matters in the real world:** Used by SOC analysts and DNS firewall vendors to catch data exfiltration over DNS.

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
cd projects/computer_science/cybersecurity/dns-tunneling-detector-log_analyzer-advanced
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
