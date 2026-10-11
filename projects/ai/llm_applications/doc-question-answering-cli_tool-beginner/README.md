# Document Q&A Assistant: Command-Line Tool

**Domain:** ai | **Subdomain:** llm_applications | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Document Q&A Assistant built as a Command-line tool. A document Q&A assistant answers natural-language questions using only the text of a supplied document, reducing hallucinations by grounding every answer in retrieved passages. The pipeline splits the document into chunks, finds the chunks most relevant to the question, and composes an answer with source references. Confidence drops gracefully when the document contains no relevant information. A subcommand CLI that generates seeded synthetic topic rows and reports summaries, top-N rows, or filtered rows as tables or JSON.

**Core concept — Document Q&A Assistant:** A document Q&A assistant answers natural-language questions using only the text of a supplied document, reducing hallucinations by grounding every answer in retrieved passages. The pipeline splits the document into chunks, finds the chunks most relevant to the question, and composes an answer with source references. Confidence drops gracefully when the document contains no relevant information.

**Why this matters in the real world:** Powers help-center bots and internal knowledge assistants that answer from company documentation.

---

## Features

- `generate_rows` (`generate_rows(seed, count)`): Generate deterministic synthetic topic rows.
- `cmd_summary` (`cmd_summary(rows, args)`): Print per-category counts and value statistics.
- `cmd_top` (`cmd_top(rows, args)`): Print the top-N rows by value.
- `cmd_filter` (`cmd_filter(rows, args)`): Print rows whose value is at least --min-value.
- `main` (`main()`): Parse args and dispatch to the chosen subcommand.

---

## Tech Stack

Python 3.8+, stdlib: argparse, json, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Deterministic synthetic rows + subcommand dispatch. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) to generate rows; O(n log n) for top-N sort. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/llm_applications/doc-question-answering-cli_tool-beginner
python3 src/main.py --help
python3 src/main.py
```
Try `python3 src/main.py top --top-n 3`, `python3 src/main.py filter --min-value 900`, or add --json to any command.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A formatted text table (or JSON with --json) for the summary, top-N, or filter subcommand.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
