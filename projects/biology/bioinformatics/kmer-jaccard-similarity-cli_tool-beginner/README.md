# K-mer Jaccard Similarity Estimator: Command-Line Tool

**Domain:** biology | **Subdomain:** bioinformatics | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

K-mer Jaccard Similarity Estimator built as a Command-line tool. K-mer Jaccard similarity estimates sequence relatedness without alignment by comparing the sets of length-k substrings; the Jaccard index is the intersection size over the union size. MinHash sketching approximates it for huge sequences. The tool computes exact Jaccard for small inputs and sketched estimates for large ones. A subcommand CLI that generates seeded synthetic topic rows and reports summaries, top-N rows, or filtered rows as tables or JSON.

**Core concept — K-mer Jaccard Similarity Estimator:** K-mer Jaccard similarity estimates sequence relatedness without alignment by comparing the sets of length-k substrings; the Jaccard index is the intersection size over the union size. MinHash sketching approximates it for huge sequences. The tool computes exact Jaccard for small inputs and sketched estimates for large ones.

**Why this matters in the real world:** K-mer similarity screens metagenomic samples and clusters massive sequence databases.

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
cd projects/biology/bioinformatics/kmer-jaccard-similarity-cli_tool-beginner
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
