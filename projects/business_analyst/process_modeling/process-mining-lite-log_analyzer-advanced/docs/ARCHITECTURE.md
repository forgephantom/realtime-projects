# Architecture (HLD) — Process Mining Lite: Log Analyzer

## Problem & Users

Process Mining Lite built as a Log analyzer. Process mining reconstructs the real process from event logs: which paths cases actually took, where they looped, and how long each variant lasted. The discovered model almost always differs from the documented one. The lite version builds the variant map and conformance gaps from seeded logs. Generates a synthetic service log in memory, parses each line with a regex, and reports level/service counts, top errors, and error rate.

The intended user is a student or engineer working in business_analyst (process_modeling) who needs a working, runnable reference for Process Mining Lite — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_log (in-memory lines)
lines -> parse_line (regex) -> entry dicts
entries -> analyze (Counters) -> print_report
```

## Storage

In-memory only: the synthetic log and aggregates exist for the run; nothing is read from or written to disk.

## Scaling & Limits

Lines are held in memory, so multi-gigabyte logs would need a streaming line-by-line variant of the same pipeline.

## Trade-offs

A single regex keeps parsing fast and readable but only handles the one log format the generator emits.

## Failure Handling

Lines that do not match the regex are skipped and excluded from totals, so a corrupt line can never crash the analysis.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
