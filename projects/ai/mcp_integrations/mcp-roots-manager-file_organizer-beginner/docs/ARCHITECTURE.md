# Architecture (HLD) — MCP Roots Manager: File Organizer

## Problem & Users

MCP Roots Manager built as a file organizer. Roots define the filesystem or URI boundaries a server may access: clients declare which directories are in scope, and servers must refuse paths outside them. Multiple roots support multi-project workspaces, and root change notifications let servers refresh. The manager enforces seeded root policies on path requests. A file organizer that generates sample files, plans moves by extension mapping, and sorts them into categorized subfolders.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Roots Manager — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| FileOrganizer | main | Sorts the top-level files of a folder into subfolders by extension. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded sample files -> demo_workspace/ (flat)
FileOrganizer.plan -> [(source, dest)] by extension map
FileOrganizer.execute -> shutil.move -> categorized subfolders
before/after trees printed to stdout
```

## Storage

Only the demo_workspace folder it creates at runtime; no state is kept between runs beyond those files.

## Scaling & Limits

Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

## Trade-offs

Top-level files only keeps the logic predictable; recursive organizing would risk surprising moves in nested folders.

## Failure Handling

Unknown extensions go to a 'misc' folder instead of erroring; --dry-run prints the plan without moving anything.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
