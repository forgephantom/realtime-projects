# Design (LLD) — Backup Verifier (Checksums): Backup Tool

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| BackupJob | Copies a source tree to a destination and verifies it with SHA-256 checksums. |

## Functions

| Function | Signature | Description |
|---|---|---|
| BackupJob.collect | collect(self) -> list | Relative paths of every file under the source, sorted. |
| BackupJob.run | run(self) -> dict | Copy every file, write a JSON manifest of SHA-256 checksums. |
| BackupJob.verify | verify(self) -> dict | Re-hash every backed-up file and compare against the manifest. |
| make_sample_files | make_sample_files(source: str, n: int, rng: random.Random) -> list | Create n seeded text and binary files under source; return rel paths. |
| run_demo | run_demo(seed: int, n_files: int, chunk_kb: int) -> int | Generate sample files, back them up with checksums, then verify. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the backup demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Backup Verifier (Checksums):

| Parameter | Meaning |
|---|---|
| schedule | backup cadence |
| verify | checksum + test-restore |
| rpo | recovery-point objective |

## Algorithm & Complexity

The core of this project is Full copy with SHA-256 manifest, then re-hash verification.

- **Time complexity:** O(bytes) to copy and hash every file
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/software_engineering/backup-verifier-checksums-backup_tool-intermediate
python3 src/main.py --help
python3 src/main.py
```
--files and --chunk-kb tune the demo. Source and backup live inside ./demo_workspace.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
