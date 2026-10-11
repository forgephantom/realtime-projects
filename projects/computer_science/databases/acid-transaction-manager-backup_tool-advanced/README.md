# ACID Transaction Manager: Backup Tool

**Domain:** computer_science | **Subdomain:** databases | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

ACID Transaction Manager built as a backup tool. ACID is the contract: atomicity (all or nothing), consistency (constraints hold), isolation (concurrent safety), durability (survives crashes). The manager implements begin/commit/rollback over a page store with WAL, demonstrating each property with failure injection. It is the database promise in code. A backup tool that copies a folder, records SHA-256 checksums in a JSON manifest, and verifies the backup by re-hashing.

**Core concept — ACID Transaction Manager:** ACID is the contract: atomicity (all or nothing), consistency (constraints hold), isolation (concurrent safety), durability (survives crashes). The manager implements begin/commit/rollback over a page store with WAL, demonstrating each property with failure injection. It is the database promise in code.

**Why this matters in the real world:** Every relational database (Postgres, MySQL, SQLite) implements the ACID contract.

---

## Features

- **BackupJob**: Copies a source tree to a destination and verifies it with SHA-256 checksums.
- `BackupJob.collect` (`collect(self) -> list`): Relative paths of every file under the source, sorted.
- `BackupJob.run` (`run(self) -> dict`): Copy every file, write a JSON manifest of SHA-256 checksums.
- `BackupJob.verify` (`verify(self) -> dict`): Re-hash every backed-up file and compare against the manifest.
- `make_sample_files` (`make_sample_files(source: str, n: int, rng: random.Random) -> list`): Create n seeded text and binary files under source; return rel paths.
- `run_demo` (`run_demo(seed: int, n_files: int, chunk_kb: int) -> int`): Generate sample files, back them up with checksums, then verify.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the backup demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, hashlib, json, os, random, shutil

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Full copy with SHA-256 manifest, then re-hash verification. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(bytes) to copy and hash every file. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/databases/acid-transaction-manager-backup_tool-advanced
python3 src/main.py --help
python3 src/main.py
```
--files and --chunk-kb tune the demo. Source and backup live inside ./demo_workspace.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-file table (name, bytes, checksum prefix), the manifest path, and the verify result (N/N OK).

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
