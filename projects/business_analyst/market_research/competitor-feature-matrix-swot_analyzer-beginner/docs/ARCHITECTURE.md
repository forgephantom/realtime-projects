# Architecture (HLD) — Competitor Feature Matrix: Swot_Analyzer

## Problem & Users

Competitor Feature Matrix built as a swot_analyzer. A competitor feature matrix lists capabilities as rows and competitors as columns, marking who has what. Gaps where nobody delivers are opportunities; rows where everyone matches are table stakes. The matrix turns scattered competitive intel into one comparable view. A SWOT and requirements analyzer that scores seeded factor lists per quadrant, finds the dominant quadrant, and generates TOWS action items.

The intended user is a student or engineer working in business_analyst (market_research) who needs a working, runnable reference for Competitor Feature Matrix — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded factor lists -> build_factors (weight, score per factor)
factors -> score_quadrant -> quadrant totals -> dominant quadrant
top factors -> tows_actions -> SO / WO / ST / WT action items
quadrants + actions -> render_matrix -> ASCII 2x2 matrix
```

## Storage

No persistence: factors are regenerated from the seed each run.

## Scaling & Limits

The math is trivial at any factor count; real use is in workshop facilitation, not computation.

## Trade-offs

Seeded factors make a reproducible demo; real analysis needs human judgment to name and weight factors.

## Failure Handling

Empty factor lists score zero and yield a 'no factors' note instead of a crash, so partial input still renders.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
