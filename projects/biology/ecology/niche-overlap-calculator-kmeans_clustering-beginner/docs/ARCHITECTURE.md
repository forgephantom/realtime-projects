# Architecture (HLD) — Niche Overlap Calculator: K-Means Clustering

## Problem & Users

Niche Overlap Calculator built as a K-means clustering. Niche overlap quantifies shared resource use between species pairs, commonly with Pianka's or Schoener's index from utilization proportions. High overlap predicts strong competition. The calculator builds the pairwise overlap matrix and clusters species by niche similarity. Runs Lloyd's k-means on seeded 2-D synthetic points and prints final centroids, cluster sizes, and inertia.

The intended user is a student or engineer working in biology (ecology) who needs a working, runnable reference for Niche Overlap Calculator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
