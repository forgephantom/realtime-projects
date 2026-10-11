# Presentation Guide — DBSCAN Density Clustering: K-Means Clustering

## 60-Second Pitch

A DBSCAN Density Clustering k-means implementation in pure Python running Lloyd's algorithm on seeded blobs, printing centroids, sizes, and inertia. DBSCAN groups points with enough neighbors within radius eps, labeling sparse regions as noise: it finds arbitrarily shaped clusters and needs no k.

DBSCAN Density Clustering in two sentences: DBSCAN groups points with enough neighbors within radius eps, labeling sparse regions as noise: it finds arbitrarily shaped clusters and needs no k. Core/border/noise classification falls out of the two parameters. Tuning eps via the k-distance plot is the practical skill the demo teaches.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Lloyd's k-means: assign, recompute, repeat until convergence; runs in O(n*k*i) for n points, k clusters, i iterations.
- Honest scaling limit: Pure-Python distance loops are O(n*k) per iteration, so large datasets would need numpy vectorization.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a DBSCAN Density Clustering k-means clustering tool in pure Python implementing Lloyd's algorithm (nearest-centroid assignment, mean recomputation) on seeded synthetic data; demo prints centroids, cluster sizes, and inertia.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are initial centroids chosen?

**A:** Random data points sampled with the seed, which is the standard k-means++-free initialization; results stay deterministic per seed.

**Q:** Is cluster quality measured?

**A:** Yes; lower inertia means tighter clusters, and the demo prints it after the final assignment.

**Q:** Can the demo shape be changed?

**A:** Use --k, --n, and --iterations to change the cluster count, point count, and iteration cap.
