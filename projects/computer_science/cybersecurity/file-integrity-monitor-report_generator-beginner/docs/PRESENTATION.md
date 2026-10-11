# Presentation Guide — File Integrity Monitor: Report Generator

## 60-Second Pitch

I built a File Integrity Monitor that turns raw measurements into a readable Markdown report with summaries you can actually act on. Rootkits and intruders modify system binaries and configs, so a file integrity monitor keeps cryptographic hashes of watched files and re-checks them on a schedule.

File Integrity Monitor in two sentences: Rootkits and intruders modify system binaries and configs, so a file integrity monitor keeps cryptographic hashes of watched files and re-checks them on a schedule. Any hash mismatch, permission change, or unexpected new file in a watched directory raises an alert with the diff of what changed. The baseline database itself is checksummed so tampering with the monitor is detectable.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded synthetic data generation, aggregation rollups, Markdown rendering; runs in O(n) to generate and summarize n records.
- Honest scaling limit: Holds all records in memory; millions of rows would want streaming aggregation instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a File Integrity Monitor in Python that aggregates seeded measurement data into summary tables and emits a Markdown report.
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
