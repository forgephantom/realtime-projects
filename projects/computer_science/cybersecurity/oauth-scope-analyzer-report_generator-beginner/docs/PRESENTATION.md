# Presentation Guide — OAuth Scope Analyzer: Report Generator

## 60-Second Pitch

I built a OAuth Scope Analyzer that turns raw measurements into a readable Markdown report with summaries you can actually act on. OAuth scopes define what a third-party app may do on a user's behalf, and over-broad grants turn a compromised app into a full account takeover.

OAuth Scope Analyzer in two sentences: OAuth scopes define what a third-party app may do on a user's behalf, and over-broad grants turn a compromised app into a full account takeover. The analyzer inventories granted scopes per application, flags sensitive combinations like read plus delete, and recommends least-privilege reductions. It also spots apps that have not been used in months.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded synthetic data generation, aggregation rollups, Markdown rendering; runs in O(n) to generate and summarize n records.
- Honest scaling limit: Holds all records in memory; millions of rows would want streaming aggregation instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a OAuth Scope Analyzer in Python that aggregates seeded measurement data into summary tables and emits a Markdown report.
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
