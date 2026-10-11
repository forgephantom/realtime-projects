# Design (LLD) — Gaussian Mixture Models (EM): K-Means Clustering

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_points | generate_points(seed, n, k) | Generate 2-D points around k random topic centers. |
| assign | assign(points, centroids) | Assign each point to its nearest centroid; return label list. |
| recompute | recompute(points, labels, k, centroids) | Recompute centroids as cluster means; keep old center if empty. |
| inertia | inertia(points, labels, centroids) | Sum of squared distances of points to their assigned centroid. |
| kmeans | kmeans(points, k, iterations, seed) | Run Lloyd's algorithm; return (centroids, labels). |
| main | main() | Parse args, cluster, and print centroids and inertia. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Gaussian Mixture Models (EM):

| Parameter | Meaning |
|---|---|
| components | number of Gaussians |
| covariance | full vs diagonal vs spherical |
| max_iter | EM iterations |

## Algorithm & Complexity

The core of this project is Lloyd's k-means: assign, recompute, repeat until convergence.

- **Time complexity:** O(n*k*i) for n points, k clusters, i iterations
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/machine_learning/gaussian-mixture-em-kmeans_clustering-intermediate
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
