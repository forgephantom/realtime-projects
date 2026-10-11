# DBSCAN Density Clustering: K-Means Clustering

**Domain:** computer_science | **Subdomain:** machine_learning | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

DBSCAN Density Clustering built as a K-means clustering. DBSCAN groups points with enough neighbors within radius eps, labeling sparse regions as noise: it finds arbitrarily shaped clusters and needs no k. Core/border/noise classification falls out of the two parameters. Tuning eps via the k-distance plot is the practical skill the demo teaches. Runs Lloyd's k-means on seeded 2-D synthetic points and prints final centroids, cluster sizes, and inertia.

**Core concept — DBSCAN Density Clustering:** DBSCAN groups points with enough neighbors within radius eps, labeling sparse regions as noise: it finds arbitrarily shaped clusters and needs no k. Core/border/noise classification falls out of the two parameters. Tuning eps via the k-distance plot is the practical skill the demo teaches.

**Why this matters in the real world:** Geospatial hotspot detection, fraud rings, and sensor anomaly grouping use DBSCAN.

---

## Features

- `generate_points` (`generate_points(seed, n, k)`): Generate 2-D points around k random topic centers.
- `assign` (`assign(points, centroids)`): Assign each point to its nearest centroid; return label list.
- `recompute` (`recompute(points, labels, k, centroids)`): Recompute centroids as cluster means; keep old center if empty.
- `inertia` (`inertia(points, labels, centroids)`): Sum of squared distances of points to their assigned centroid.
- `kmeans` (`kmeans(points, k, iterations, seed)`): Run Lloyd's algorithm; return (centroids, labels).
- `main` (`main()`): Parse args, cluster, and print centroids and inertia.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Lloyd's k-means: assign, recompute, repeat until convergence. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n*k*i) for n points, k clusters, i iterations. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/machine_learning/dbscan-density-clustering-kmeans_clustering-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A cluster table (id, centroid x/y, size) and the final inertia value.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
