# Rule-Based Signal Peptide Predictor: Command-Line Tool

**Domain:** biology | **Subdomain:** bioinformatics | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Rule-Based Signal Peptide Predictor built as a Command-line tool. Signal peptides are N-terminal stretches with a positively charged n-region, hydrophobic h-region, and cleavage site that direct proteins to the secretory pathway. A rule-based predictor scores these regions with hydrophobicity windows and cleavage-site patterns. It reports the predicted cleavage position and a secretion verdict. A subcommand CLI that generates seeded synthetic topic rows and reports summaries, top-N rows, or filtered rows as tables or JSON.

**Core concept — Rule-Based Signal Peptide Predictor:** Signal peptides are N-terminal stretches with a positively charged n-region, hydrophobic h-region, and cleavage site that direct proteins to the secretory pathway. A rule-based predictor scores these regions with hydrophobicity windows and cleavage-site patterns. It reports the predicted cleavage position and a secretion verdict.

**Why this matters in the real world:** Signal-peptide prediction (SignalP) triages secreted proteins in drug-target discovery.

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
cd projects/biology/bioinformatics/signal-peptide-predictor-cli_tool-intermediate
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
