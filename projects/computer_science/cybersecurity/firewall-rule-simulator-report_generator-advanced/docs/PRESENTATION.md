# Presentation Guide — Firewall Rule Simulator: Report Generator

## 60-Second Pitch

I built a Firewall Rule Simulator that turns raw measurements into a readable Markdown report with summaries you can actually act on. Firewall policies are ordered rule lists where the first match wins, and a misplaced permissive rule can silently shadow stricter ones below it.

Firewall Rule Simulator in two sentences: Firewall policies are ordered rule lists where the first match wins, and a misplaced permissive rule can silently shadow stricter ones below it. The simulator evaluates packets against a rule set, shows exactly which rule matched and why, and audits the policy for shadowed rules, overly broad allows, and default-deny gaps. It lets engineers test policy changes safely before pushing them to production.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded synthetic data generation, aggregation rollups, Markdown rendering; runs in O(n) to generate and summarize n records.
- Honest scaling limit: Holds all records in memory; millions of rows would want streaming aggregation instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Firewall Rule Simulator in Python that aggregates seeded measurement data into summary tables and emits a Markdown report.
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
