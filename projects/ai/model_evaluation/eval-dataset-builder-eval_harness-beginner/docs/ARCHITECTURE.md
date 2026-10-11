# Architecture (HLD) — Evaluation Dataset Builder: Eval_Harness

## Problem & Users

Evaluation Dataset Builder built as a eval_harness. A good eval set covers the task space: difficulty tiers, edge cases, and categories the model must not regress on. This tool builds seeded question-answer sets with metadata tags, deduplicates near-identical items, and computes coverage stats over categories. Stratified sampling keeps small sets representative of the full distribution. An evaluation harness that runs test cases against a stub model, measures accuracy and latency, and adds an LLM-as-judge rubric score per case.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Evaluation Dataset Builder — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
test cases -> run_case (stub model + latency + exact match) -> results
results + rubric -> judge_score per case -> judged scores
results + judged -> summarize -> accuracy, latency, judge averages
```

## Storage

No persistence: cases, results, and summaries are regenerated from the seed each run.

## Scaling & Limits

Sequential runs suit hundreds of cases; thousands would want parallel workers and a persistent results store.

## Trade-offs

Exact-match correctness is strict and reproducible but penalizes correct answers phrased differently; the judge score softens that.

## Failure Handling

A stub model crash is caught per case and recorded as incorrect with the error text, so one bad case never kills the run.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
