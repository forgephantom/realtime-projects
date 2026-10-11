# Columnar Storage Demo: File Organizer

**Domain:** computer_science | **Subdomain:** databases | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Columnar Storage Demo built as a file organizer. Columnar layouts store each column contiguously: scans over few columns touch little data, and same-type values compress well (RLE, dictionary). The demo builds column chunks with encodings and runs analytical queries against them. It is why warehouses are fast at aggregations. A file organizer that generates sample files, plans moves by extension mapping, and sorts them into categorized subfolders.

**Core concept — Columnar Storage Demo:** Columnar layouts store each column contiguously: scans over few columns touch little data, and same-type values compress well (RLE, dictionary). The demo builds column chunks with encodings and runs analytical queries against them. It is why warehouses are fast at aggregations.

**Why this matters in the real world:** Parquet, ClickHouse, and Snowflake store columns for analytics.

---

## Features

- **FileOrganizer**: Sorts the top-level files of a folder into subfolders by extension.
- `FileOrganizer.category_for` (`category_for(self, filename: str) -> str`): Folder name for a file's extension, or 'misc' when unknown.
- `FileOrganizer.plan` (`plan(self) -> list`): [(source, destination), ...] for every top-level file in root.
- `FileOrganizer.execute` (`execute(self, plan: list) -> list`): Carry out a plan from plan(); return the moves that happened.
- `FileOrganizer.report` (`report(self, moves: list) -> str`): One-line-per-move human-readable summary.
- `make_sample_files` (`make_sample_files(root: str, n: int, rng: random.Random) -> list`): Create n seeded sample files directly inside root; return their names.
- `list_tree` (`list_tree(root: str) -> list`): Relative paths of everything under root, directories first, sorted.
- `run_demo` (`run_demo(seed: int, n_files: int, dry_run: bool) -> int`): Generate sample files, show before/after, then organize them.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the organizer demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, os, random, shutil

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Extension-to-folder mapping with a plan-then-execute move pass. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(f) over f files. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/databases/columnar-storage-demo-file_organizer-advanced
python3 src/main.py --help
python3 src/main.py
```
--files sets the sample count; --dry-run prints the move plan without moving anything. Works inside ./demo_workspace.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints before/after directory trees of demo_workspace plus the move plan and moved-file count.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
