# Architecture (HLD) — Habit Moment Finder: K-Means Clustering

## Problem & Users

Habit Moment Finder built as a K-means clustering. Habit formation shows in frequency distributions: the finder clusters users by usage cadence and finds the frequency threshold where retention jumps (the habit moment). It is correlational but powerfully directional for product design. Weekly-vs-daily patterns emerge from the data. Runs Lloyd's k-means on seeded 2-D synthetic points and prints final centroids, cluster sizes, and inertia.

The intended user is a student or engineer working in computer_science (data_science) who needs a working, runnable reference for Habit Moment Finder — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_points (k Gaussian blobs)
points -> kmeans: assign -> recompute -> ...
(centroids, labels) -> inertia + cluster table
```

## Storage

In-memory only: points, centroids, and labels exist for the run and are not persisted.

## Scaling & Limits

Pure-Python distance loops are O(n*k) per iteration, so large datasets would need numpy vectorization.

## Trade-offs

Hand-written Lloyd's is transparent and dependency-free, but lacks k-means++ seeding and mini-batch variants for big data.

## Failure Handling

An empty cluster keeps its previous centroid instead of producing NaNs; iteration stops early when centroids stop moving.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
