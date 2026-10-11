# Architecture (HLD) — NFR Cataloger: Report Generator

## Problem & Users

NFR Cataloger built as a report generator. Non-functional requirements cover performance, security, reliability, and usability: the qualities that make software acceptable rather than just functional. They must be measurable, like response under two seconds at peak load, or they are unenforceable. A cataloger collects them by quality attribute and attaches a metric to each. A report generator that builds seeded synthetic data, aggregates it, and writes a Markdown report with summary and per-service tables.

The intended user is a student or engineer working in business_analyst (requirements_management) who needs a working, runnable reference for NFR Cataloger — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded RNG -> generate_records -> list of measurement dicts
records -> summarize -> totals, per-service rollups, error rate
summary + sample rows -> render_markdown -> demo_output/report.md
```

## Storage

Writes one Markdown file under ./demo_output; nothing else is persisted.

## Scaling & Limits

Holds all records in memory; millions of rows would want streaming aggregation instead.

## Trade-offs

Hand-rolled Markdown keeps the demo dependency-free; a real reporting tool might use a templating engine.

## Failure Handling

No external input is parsed, so there is nothing malformed to handle; write errors propagate as normal OSErrors.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
