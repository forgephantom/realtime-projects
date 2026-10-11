# Presentation Guide — High-Throughput Screen Analyzer: Report Generator

## 60-Second Pitch

I built a High-Throughput Screen Analyzer that turns raw measurements into a readable Markdown report with summaries you can actually act on. High-throughput screening analysis starts with plate normalization against controls, then calls hits beyond a standard-deviation threshold.

High-Throughput Screen Analyzer in two sentences: High-throughput screening analysis starts with plate normalization against controls, then calls hits beyond a standard-deviation threshold. The Z-prime factor quantifies assay quality from the separation between positive and negative controls. Synthetic plates with planted hits let analysts verify normalization and hit-calling end to end.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded synthetic data generation, aggregation rollups, Markdown rendering; runs in O(n) to generate and summarize n records.
- Honest scaling limit: Holds all records in memory; millions of rows would want streaming aggregation instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a High-Throughput Screen Analyzer in Python that aggregates seeded measurement data into summary tables and emits a Markdown report.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What aggregations does it compute?

**A:** summarize() rolls up requests, errors, and max p99 latency per service, plus overall totals and the error rate.

**Q:** Is the data real?

**A:** A seeded RNG produces the same dataset on every run, so the report is reproducible byte-for-byte for a given seed.

**Q:** What would change for production data?

**A:** The generator hardcodes a small service list and date window; a real version would read from logs or a database.
