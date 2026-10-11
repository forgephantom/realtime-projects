# Architecture (HLD) — K-Means Scan Segmentation: K-Means Clustering

## Problem & Users

K-Means Scan Segmentation built as a K-means clustering. K-means clustering groups pixels by intensity, optionally including spatial coordinates, into a fixed number of tissue classes. Random initialization makes results vary, so multiple restarts with the best inertia are standard practice. Cluster purity against known phantom labels shows how well the unsupervised split matches real tissue boundaries. Runs Lloyd's k-means on seeded 2-D synthetic points and prints final centroids, cluster sizes, and inertia.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for K-Means Scan Segmentation — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
