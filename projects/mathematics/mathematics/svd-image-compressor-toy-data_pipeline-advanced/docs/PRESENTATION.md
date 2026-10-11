# Presentation Guide — Toy SVD Rank Compressor: Data Pipeline (Etl)

## 60-Second Pitch

A Toy SVD Rank Compressor ETL pipeline that extracts seeded records, cleans and buckets them, loads a CSV, and reports every stage count. The singular value decomposition writes a matrix as U Sigma V^T, and keeping only the top k singular values gives the best rank-k approximation in Frobenius norm.

Toy SVD Rank Compressor in two sentences: The singular value decomposition writes a matrix as U Sigma V^T, and keeping only the top k singular values gives the best rank-k approximation in Frobenius norm. Truncating small singular values compresses image-like data dramatically. This toy pipeline computes a small SVD by eigendecomposition of the Gram matrix and reconstructs approximations.

## Architecture Talking Points

- Components: `Pipeline` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extract -> transform -> load over synthetic records; runs in O(n) across all three stages.
- Honest scaling limit: All rows are held in memory between stages, so very large inputs would need chunked or streaming processing instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Toy SVD Rank Compressor ETL pipeline in Python (stdlib csv) with extract, transform, and load stages; handles corrupt rows with drop counts and reports per-stage statistics to the console.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Does the pipeline need a real data source?

**A:** No; generate_raw synthesizes deterministic rows from the seed, so the pipeline demonstrates all three stages with zero external input.

**Q:** How are corrupt rows handled?

**A:** clean_rows drops them, counts the drops, and reports the number in the stage report.

**Q:** Does it write files?

**A:** Yes; it is the only file write, and it stays inside the current working directory under demo_workspace/.
