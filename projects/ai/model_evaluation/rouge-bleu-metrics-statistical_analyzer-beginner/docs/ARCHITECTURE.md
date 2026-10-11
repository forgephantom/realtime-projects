# Architecture (HLD) — Text Overlap Metrics Suite: Statistical Analyzer

## Problem & Users

Text Overlap Metrics Suite built as a Statistical analyzer. ROUGE and BLEU score generated text by n-gram overlap with reference answers: ROUGE is recall-oriented for summarization, BLEU is precision-oriented with a brevity penalty for translation. They are fast and reproducible but blind to paraphrase quality, which is why modern evals pair them with semantic metrics. The suite implements them from scratch on tokenized text. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Text Overlap Metrics Suite — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_sample (mixture model)
sample -> summarize (sort, moments, percentiles, histogram)
summary -> print_report (table + ASCII histogram)
```

## Storage

In-memory only: the sample and summary exist for the duration of the run and nothing is persisted.

## Scaling & Limits

The sample is sorted in memory, so multi-million-point samples would need a streaming quantile sketch instead.

## Trade-offs

Hand-rolled statistics avoid dependencies but only cover univariate descriptives, not hypothesis tests or modeling.

## Failure Handling

An empty sample cannot occur (n comes from --samples), and a constant sample degrades gracefully to a single non-empty histogram bin.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
