# Presentation Guide — Evaluation Report Generator: Eval_Harness

## 60-Second Pitch

I built a Evaluation Report Generator that grades model answers for accuracy and latency and adds an LLM-as-judge rubric score per case. Eval results only matter if stakeholders can read them: the report generator turns raw run JSON into summary tables, per-category breakdowns, significance notes, and trend charts against prior runs.

Evaluation Report Generator in two sentences: Eval results only matter if stakeholders can read them: the report generator turns raw run JSON into summary tables, per-category breakdowns, significance notes, and trend charts against prior runs. Templated sections keep every report comparable, and a headline verdict answers whether the release bar was met.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Each case runs a seeded stub model with latency timing, correctness is exact-match, and an LLM-as-judge rubric scores the output text.; runs in O(N) over N test cases; each case is one stub call plus rubric checks..
- Honest scaling limit: Sequential runs suit hundreds of cases; thousands would want parallel workers and a persistent results store.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Evaluation Report Generator in Python with seeded test cases, latency measurement, and an LLM-as-judge rubric scorer.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What does the stub model do?

**A:** A deterministic stub: correct unless a hash of the case id hits the 25 percent bucket, where it answers off by one.

**Q:** What is the judge score?

**A:** It simulates rubric grading with keyword checks and a length penalty, giving a second quality signal beyond exact match.

**Q:** Can this evaluate a real model?

**A:** Swap stub_model for a real model call; run_case, judge_score, and summarize are backend-agnostic.
