# SSH Brute-Force Log Detector: Log Analyzer

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

SSH Brute-Force Log Detector built as a Log analyzer. Attackers guess SSH credentials by trying many username and password pairs against port 22, which leaves a trail of failed password lines in the auth log. The detector parses those log lines, groups failures by source IP and username, and raises an alert when the failure rate exceeds a policy, distinguishing slow stealthy guessing from noisy bursts. It can emit ready-to-use blocklist entries for fail2ban style tooling. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — SSH Brute-Force Log Detector:** Attackers guess SSH credentials by trying many username and password pairs against port 22, which leaves a trail of failed password lines in the auth log. The detector parses those log lines, groups failures by source IP and username, and raises an alert when the failure rate exceeds a policy, distinguishing slow stealthy guessing from noisy bursts. It can emit ready-to-use blocklist entries for fail2ban style tooling.

**Why this matters in the real world:** Used by sysadmins and SOC analysts to catch credential-guessing campaigns against Linux servers.

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
cd projects/computer_science/cybersecurity/ssh-brute-force-log-detector-log_analyzer-beginner
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
