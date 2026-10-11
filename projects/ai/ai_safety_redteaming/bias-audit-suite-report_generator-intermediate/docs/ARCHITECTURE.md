# Architecture (HLD) — Bias and Fairness Audit Suite: Report Generator

## Problem & Users

Bias and Fairness Audit Suite built as a report generator. Bias audits test whether a model treats demographic groups differently: counterfactual pairs swap group references while holding everything else fixed, and score gaps reveal disparate treatment. Fairness metrics like demographic parity and equalized odds quantify the gaps on seeded tasks. Reports include per-group breakdowns and remediation notes. A report generator that builds seeded synthetic data, aggregates it, and writes a Markdown report with summary and per-service tables.

The intended user is a student or engineer working in ai (ai_safety_redteaming) who needs a working, runnable reference for Bias and Fairness Audit Suite — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
