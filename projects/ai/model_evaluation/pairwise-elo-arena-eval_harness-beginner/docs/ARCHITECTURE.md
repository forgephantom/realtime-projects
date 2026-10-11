# Architecture (HLD) — Pairwise Elo Rating Arena: Eval_Harness

## Problem & Users

Pairwise Elo Rating Arena built as a eval_harness. In a pairwise arena, judges pick the better of two model responses and Elo ratings update from wins and losses, exactly like chess rankings. The expected-score formula turns rating gaps into win probabilities, and the K-factor controls how fast ratings move. Seeded win histories let you verify the ratings converge on the true skill order. An evaluation harness that runs test cases against a stub model, measures accuracy and latency, and adds an LLM-as-judge rubric score per case.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Pairwise Elo Rating Arena — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
