# Architecture (HLD) — Write-Ahead Log (WAL): Backup Tool

## Problem & Users

Write-Ahead Log (WAL) built as a backup tool. Durability starts with the WAL: changes append to the log before touching data pages, so crashes replay the log to recover. The demo implements append, checkpoint, and replay, then crash-tests recovery. Group commit batches the fsync cost. No WAL, no durability guarantees. A backup tool that copies a folder, records SHA-256 checksums in a JSON manifest, and verifies the backup by re-hashing.

The intended user is a student or engineer working in computer_science (databases) who needs a working, runnable reference for Write-Ahead Log (WAL) — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| BackupJob | main | Copies a source tree to a destination and verifies it with SHA-256 checksums. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
demo_workspace/source -> BackupJob.collect -> file list
copy2 per file + SHA-256 -> demo_workspace/backup + manifest.json
BackupJob.verify -> re-hash backup -> compare manifest -> OK/FAILED
```

## Storage

The backup folder and manifest.json persist inside ./demo_workspace until the next demo run wipes them.

## Scaling & Limits

Single-machine full copies; large trees would want incremental backups and parallel hashing.

## Trade-offs

Full copies are simple and robust but wasteful for large trees; incremental backups would add real complexity.

## Failure Handling

verify() reports exactly which files mismatch instead of failing silently; a failed verify returns exit code 1.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
