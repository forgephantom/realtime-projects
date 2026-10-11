# Architecture (HLD) — Compound Cluster Visualizer: K-Means Clustering

## Problem & Users

Compound Cluster Visualizer built as a K-means clustering. Clustering compounds by fingerprint similarity groups a library into chemotypes, and picking one representative per cluster yields a diverse subset for screening. The similarity cutoff controls the granularity: too high fragments the library, too low merges distinct chemistry. Visualizing clusters with known planted structure validates the approach. Runs Lloyd's k-means on seeded 2-D synthetic points and prints final centroids, cluster sizes, and inertia.

The intended user is a student or engineer working in healthcare (drug_discovery) who needs a working, runnable reference for Compound Cluster Visualizer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
