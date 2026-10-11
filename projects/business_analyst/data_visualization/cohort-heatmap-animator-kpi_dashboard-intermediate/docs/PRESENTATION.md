# Presentation Guide — Cohort Heatmap Animator: Kpi_Dashboard

## 60-Second Pitch

I built a Cohort Heatmap Animator that turns raw business series into growth, churn, CAC, and LTV on one ASCII dashboard. An animated cohort heatmap plays retention forward month by month, so viewers watch cohorts fade or hold over time.

Cohort Heatmap Animator in two sentences: An animated cohort heatmap plays retention forward month by month, so viewers watch cohorts fade or hold over time. Animation adds the time dimension a static heatmap compresses. It is particularly persuasive for showing that a product change bent the retention curve.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded geometric-growth business series; KPIs from period ratios: growth, churn, CAC, and LTV from ARPU over churn.; runs in O(M) over M months of synthetic data; all KPI math is O(1) on aggregates..
- Honest scaling limit: In-memory series suit dashboard demos; production use would stream aggregates from a warehouse.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Cohort Heatmap Animator in Python computing growth, churn, CAC, and LTV from synthetic business data with an ASCII dashboard.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is CAC computed?

**A:** Total marketing spend divided by total new customers; with zero new customers it reports infinity instead of crashing.

**Q:** How is LTV computed?

**A:** Average revenue per user divided by the churn rate, the standard payback-style lifetime estimate.

**Q:** Can it use real data?

**A:** Yes: generate_business_data only makes the demo series; compute_kpis works on any dict with the same keys.
