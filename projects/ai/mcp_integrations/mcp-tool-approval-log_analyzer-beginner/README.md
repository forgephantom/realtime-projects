# MCP Tool Approval Gate: Log Analyzer

**Domain:** ai | **Subdomain:** mcp_integrations | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

MCP Tool Approval Gate built as a Log analyzer. Tool approval gates pause sensitive tool calls for human confirmation: the client shows what the tool will do, the user approves or denies, and the decision is logged for audit. Policies auto-approve low-risk reads while always gating writes and external actions. The gate simulates seeded approval flows with risk tiers. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

**Core concept — MCP Tool Approval Gate:** Tool approval gates pause sensitive tool calls for human confirmation: the client shows what the tool will do, the user approves or denies, and the decision is logged for audit. Policies auto-approve low-risk reads while always gating writes and external actions. The gate simulates seeded approval flows with risk tiers.

**Why this matters in the real world:** Agent products ask permission before tools modify files or send data.

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
cd projects/ai/mcp_integrations/mcp-tool-approval-log_analyzer-beginner
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
