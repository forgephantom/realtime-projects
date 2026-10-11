# Multipart Form Parser: File Organizer

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Multipart Form Parser built as a file organizer. File uploads arrive as multipart/form-data: the parser splits the body on the boundary delimiter, extracts each part's headers and disposition, and streams file parts to disk without loading them fully into memory. It must enforce per-part and total size limits and handle boundary edge cases. Getting streaming right is what separates production parsers from tutorials. A file organizer that generates sample files, plans moves by extension mapping, and sorts them into categorized subfolders.

**Core concept — Multipart Form Parser:** File uploads arrive as multipart/form-data: the parser splits the body on the boundary delimiter, extracts each part's headers and disposition, and streams file parts to disk without loading them fully into memory. It must enforce per-part and total size limits and handle boundary edge cases. Getting streaming right is what separates production parsers from tutorials.

**Why this matters in the real world:** Every web framework's upload handling (Express multer, Django, Flask) implements multipart parsing.

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
cd projects/computer_science/web_development/multipart-form-parser-file_organizer-beginner
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
