# Resume Guide: Listing These Projects

These projects are real, runnable work — they belong on a resume. But a resume
is a claim about *you*, not about the repository. This guide shows how to
present them honestly and effectively.

## Where to put them

- **One "Projects" section**, after Experience and before or after Skills
  depending on which is stronger for the role. Never scatter projects between
  job entries.
- **One line per project**: name, one-line description, tech. Link the repo or
  the live demo if you have one.
- **Two to four projects maximum** on a one-page resume. Pick the ones closest
  to the job description; the rest live behind the repo link.

## How to adapt the per-project resume bullet

Each project's PRESENTATION.md ships a resume bullet. It is a starting draft,
not a finished line. Adapt it in three steps:

1. **Lead with the outcome**, not the activity. "Cut query latency 40%" beats
   "Built a tool that optimizes queries" — if the project measured something,
   say the number.
2. **Name the mechanism once.** One technical term that proves depth
   ("using consistent hashing", "with a seeded Monte Carlo simulation").
   Two terms is clutter; zero is a claim without evidence.
3. **Match the job's vocabulary.** If the posting says "distributed systems"
   and your bullet says "parallel processing," change your bullet. Same work,
   their words.

## Three before/after examples

**Example 1 — vague activity → measured outcome**

- Before: "Built a Python project for sorting algorithms with visualization."
- After: "Built a sorting-algorithm visualizer in pure Python that benchmarks
  6 algorithms on seeded datasets and renders step-by-step comparisons;
  documented with HLD/LLD and a 3-minute demo runbook."

**Example 2 — tech list → problem solved**

- Before: "Created a REST API project using Python, JSON, and HTTP."
- After: "Designed and built a rate-limited task-queue API (stdlib only, no
  frameworks) handling 10k queued jobs in the seeded demo; wrote the
  architecture doc covering the token-bucket trade-off vs. fixed windows."

**Example 3 — course-like → engineering-like**

- Before: "Did a machine learning project on customer segmentation."
- After: "Implemented k-means clustering from scratch in Python (no ML
  libraries) on synthetic customer data; demo converges in under 5 seconds
  and the design doc records the initialization trade-off tested."

## What NOT to claim

- **Do not claim production use.** These are engineered demos, not production
  systems. "Built" is honest; "deployed to production" is not.
- **Do not claim scale you did not measure.** If the demo processed 10,000
  records, say 10,000 — not "large-scale" or "big data."
- **Do not claim collaboration you did not do.** Solo-built means solo-built;
  there is no penalty for it.
- **Do not paste the bullet verbatim for every job.** A bullet tuned to the
  posting beats a generic one every time — that is what the adaptation steps
  above are for.
- **Do not list more projects than you can discuss.** Every line on your
  resume is an invitation to a five-minute interrogation. If you cannot whiteboard
  the project's architecture from memory, take it off.
