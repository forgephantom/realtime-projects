# Presentation Guide — Vector Index Benchmark: Vector_Db_Sim

## 60-Second Pitch

I built a Vector Index Benchmark that stores embeddings with metadata and finds the nearest neighbors by cosine similarity. A vector index benchmark measures queries per second, recall, and build time across index configurations on the same dataset.

Vector Index Benchmark in two sentences: A vector index benchmark measures queries per second, recall, and build time across index configurations on the same dataset. Standardized workloads make configurations comparable. The report recommends a configuration per latency budget.

## Architecture Talking Points

- Components: `VectorDB` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Brute-force cosine similarity over stored vectors with a JSON-serialized index for save/load.; runs in O(N*D) per search over N vectors of dimension D; add is O(D)..
- Honest scaling limit: Brute-force scan suits tens of thousands of vectors; millions would need an approximate index like HNSW.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Vector Index Benchmark in Python with cosine-similarity top-k search and JSON index persistence over seeded vector clusters.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is similarity computed?

**A:** The dot product of the two vectors divided by the product of their lengths, so scores always land between -1 and 1.

**Q:** How is the index persisted?

**A:** The whole index is serialized to one JSON file with save() and rebuilt with the VectorDB.load() classmethod.

**Q:** What happens on a bad vector?

**A:** It raises a ValueError on dimension mismatch, protecting the index from silently wrong results.
