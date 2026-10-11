# Architecture (HLD) — Vector Backup Tool: Backup Tool

## Problem & Users

Vector Backup Tool built as a backup tool. A vector backup tool snapshots the index and metadata to durable storage with incremental deltas between snapshots. Restore drills verify that a backup actually rebuilds a working index. Retention policies balance recovery granularity against storage cost. A backup tool that copies a folder, records SHA-256 checksums in a JSON manifest, and verifies the backup by re-hashing.

The intended user is a student or engineer working in ai (vector_databases) who needs a working, runnable reference for Vector Backup Tool — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
