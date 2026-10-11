# Presentation Guide — Toy SVD Rank Compressor: Web Dashboard

## 60-Second Pitch

A zero-dependency Toy SVD Rank Compressor dashboard that renders live metrics as HTML and JSON, verified end to end by its own self-test. The singular value decomposition writes a matrix as U Sigma V^T, and keeping only the top k singular values gives the best rank-k approximation in Frobenius norm.

Toy SVD Rank Compressor in two sentences: The singular value decomposition writes a matrix as U Sigma V^T, and keeping only the top k singular values gives the best rank-k approximation in Frobenius norm. Truncating small singular values compresses image-like data dramatically. This toy pipeline computes a small SVD by eigendecomposition of the Gram matrix and reconstructs approximations.

## Architecture Talking Points

- Components: `DashboardHandler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Server-side HTML rendering of a metrics table; runs in O(n) to render n metric rows.
- Honest scaling limit: Single-process threaded server rendering small pages; fine for local demos, not for high-traffic or large metric sets.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Toy SVD Rank Compressor web dashboard in Python (stdlib http.server) rendering a server-side HTML metrics table with a JSON API; default run self-tests both endpoints on 127.0.0.1 and prints verification results.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Does the page need JavaScript?

**A:** No; the table is rendered server-side as plain HTML, with a meta refresh tag for periodic updates.

**Q:** Where do the metrics come from?

**A:** A seeded RNG generates deterministic synthetic rows, so the dashboard is reproducible without any external data source.

**Q:** Can it serve persistently?

**A:** Yes, pass --serve to keep the ThreadingHTTPServer running on 127.0.0.1 until interrupted.
