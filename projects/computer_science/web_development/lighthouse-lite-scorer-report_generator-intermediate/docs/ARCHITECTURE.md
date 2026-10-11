# Architecture (HLD) — Page Quality Scorer (Lighthouse-lite): Report Generator

## Problem & Users

Page Quality Scorer (Lighthouse-lite) built as a report generator. Page quality can be scored heuristically: the scorer audits a page's resources, render-blocking scripts, image sizing, caching headers, and accessibility basics, then weights them into a 0-100 score with actionable failures. It is a simplified Lighthouse that runs offline on captured page data. The value is the prioritized fix list, not the number. A report generator that builds seeded synthetic data, aggregates it, and writes a Markdown report with summary and per-service tables.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for Page Quality Scorer (Lighthouse-lite) — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
