#!/usr/bin/env python3
"""Error Clustering Engine: K-Means Clustering: k-means clustering (Lloyd's algorithm) for Error Clustering Engine.

Thousands of error instances usually reduce to a handful of root causes, and clustering finds them. The engine groups errors by normalized message, stack signature, and context, ranking clusters by frequency and blast radius. Triage starts with clusters, not instances.
Data idea: A seeded RNG generates error streams from a few underlying bugs.

Generates deterministic 2-D Error Clustering Engine points around random centers,
runs Lloyd's algorithm (assign, recompute, repeat), and prints the final
centroids, cluster sizes, and inertia.
"""

import argparse
import random

PARAMS = {'features': 'message, stack, context used', 'similarity': 'grouping threshold', 'min_cluster': 'smallest cluster reported', 'ranking': 'frequency versus impact'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_points(seed, n, k):
    """Generate `n` 2-D points around `k` random Error Clustering Engine centers."""
    rng = random.Random(seed)
    centers = [(rng.uniform(-10.0, 10.0), rng.uniform(-10.0, 10.0))
               for _ in range(k)]
    points = []
    for _ in range(n):
        cx, cy = rng.choice(centers)
        points.append((rng.gauss(cx, 1.5), rng.gauss(cy, 1.5)))
    return points


def assign(points, centroids):
    """Assign each point to its nearest centroid; return label list."""
    labels = []
    for px, py in points:
        best, best_d = 0, float("inf")
        for i, (cx, cy) in enumerate(centroids):
            d = (px - cx) ** 2 + (py - cy) ** 2
            if d < best_d:
                best, best_d = i, d
        labels.append(best)
    return labels


def recompute(points, labels, k, centroids):
    """Recompute centroids as cluster means; keep old center if empty."""
    new_centroids = []
    for i in range(k):
        members = [p for p, lab in zip(points, labels) if lab == i]
        if members:
            new_centroids.append((
                sum(p[0] for p in members) / len(members),
                sum(p[1] for p in members) / len(members),
            ))
        else:
            new_centroids.append(centroids[i])
    return new_centroids


def inertia(points, labels, centroids):
    """Sum of squared distances of points to their assigned centroid."""
    return sum((p[0] - centroids[lab][0]) ** 2
               + (p[1] - centroids[lab][1]) ** 2
               for p, lab in zip(points, labels))


def kmeans(points, k, iterations, seed):
    """Run Lloyd's algorithm; return (centroids, labels)."""
    rng = random.Random(seed)
    centroids = rng.sample(points, k)
    labels = []
    for _ in range(iterations):
        labels = assign(points, centroids)
        moved = recompute(points, labels, k, centroids)
        if all(abs(a - b) < 1e-9
               for c1, c2 in zip(centroids, moved)
               for a, b in zip(c1, c2)):
            centroids = moved
            break
        centroids = moved
    return centroids, labels


def main():
    parser = argparse.ArgumentParser(
        description="Error Clustering Engine: K-Means Clustering: k-means for Error Clustering Engine.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--k", type=int, default=_num(PARAMS.get("k"), 3),
                        help="number of clusters")
    parser.add_argument("--n", type=int, default=_num(PARAMS.get("n"), 200),
                        help="synthetic points to generate")
    parser.add_argument("--iterations", type=int,
                        default=_num(PARAMS.get("iterations"), 12),
                        help="max Lloyd iterations")
    args = parser.parse_args()
    random.seed(args.seed)

    points = generate_points(args.seed, args.n, args.k)
    centroids, labels = kmeans(points, args.k, args.iterations, args.seed)
    cost = inertia(points, labels, centroids)
    sizes = [labels.count(i) for i in range(args.k)]

    print("Error Clustering Engine k-means (k={}, n={})".format(args.k, args.n))
    print("{:<8} {:>10} {:>10} {:>8}".format(
        "CLUSTER", "CENTROID_X", "CENTROID_Y", "SIZE"))
    for i, (cx, cy) in enumerate(centroids):
        print("{:<8} {:>10.3f} {:>10.3f} {:>8}".format(i, cx, cy, sizes[i]))
    print("inertia: {:.3f}".format(cost))


if __name__ == "__main__":
    main()
