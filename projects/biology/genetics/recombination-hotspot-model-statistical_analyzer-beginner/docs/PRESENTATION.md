# Presentation Guide — Recombination Hotspot Model: Statistical Analyzer

## 60-Second Pitch

A Recombination Hotspot Model statistics tool that turns a seeded synthetic sample into a full descriptive report with quartiles and an ASCII histogram. Recombination concentrates in hotspots, short regions with far higher crossover rates than background, shaped by PRDM9 binding in mammals.

Recombination Hotspot Model in two sentences: Recombination concentrates in hotspots, short regions with far higher crossover rates than background, shaped by PRDM9 binding in mammals. The model places crossovers with a hotspot-modulated rate along a chromosome and reports hotspot usage statistics. It compares observed versus uniform crossover spacing.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Descriptive statistics with linear-interpolation percentiles; runs in O(n log n) for the sort; O(n) for the histogram pass.
- Honest scaling limit: The sample is sorted in memory, so multi-million-point samples would need a streaming quantile sketch instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Recombination Hotspot Model statistical analyzer in pure Python computing mean, median, stdev, quartiles, and histograms from seeded synthetic data; prints a formatted report with an ASCII distribution plot.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What distribution does the sample follow?

**A:** A two-component Gaussian mixture, which gives the histogram a visible bimodal shape instead of a flat bell curve.

**Q:** Are the sample size and bins configurable?

**A:** Yes; pass --samples and --bins to control the draw size and histogram resolution.

**Q:** Does it save the report anywhere?

**A:** No; it prints to stdout only, so results can be redirected or piped freely.
