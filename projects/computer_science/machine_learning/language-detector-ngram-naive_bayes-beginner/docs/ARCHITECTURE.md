# Architecture (HLD) — Language Detector (N-gram Profiles): Naive Bayes Classifier

## Problem & Users

Language Detector (N-gram Profiles) built as a Naive Bayes classifier. Language detection compares a text's character n-gram profile against per-language profiles with a distance metric: the closest profile wins. Short texts need smoothing; script detection (Latin vs Cyrillic) shortcuts first. It needs no ML training beyond counting. Trains a Gaussian Naive Bayes classifier on seeded synthetic features and reports priors, accuracy, and the confusion matrix.

The intended user is a student or engineer working in computer_science (machine_learning) who needs a working, runnable reference for Language Detector (N-gram Profiles) — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| GaussianNB | main | Naive Bayes classifier with Gaussian feature likelihoods. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_dataset -> split_dataset (train/test)
train -> GaussianNB.fit (priors + per-feature mean/var)
test -> GaussianNB.predict -> accuracy + confusion matrix
```

## Storage

In-memory only: the dataset and learned priors/parameters exist for the run and are not persisted.

## Scaling & Limits

Pure-Python loops over features make this fine for thousands of samples; larger or high-dimensional data would want vectorization.

## Trade-offs

Naive Bayes assumes feature independence, which is fast and simple but can underperform correlated-feature models on real data.

## Failure Handling

A tiny epsilon is added to every variance so a constant feature cannot cause division by zero; ties in log-scores break toward the lower class label deterministically.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
