# Presentation Guide — Quantile Regression (Lite): Linear Regression

## 60-Second Pitch

A Quantile Regression (Lite) linear regression in pure Python that generates noisy data with a known line, recovers it with closed-form least squares, and shows the fit quality with R^2. OLS models the mean; quantile regression models any quantile (median, 90th percentile) via pinball loss, revealing how effects differ across the distribution.

Quantile Regression (Lite) in two sentences: OLS models the mean; quantile regression models any quantile (median, 90th percentile) via pinball loss, revealing how effects differ across the distribution. It is robust to outliers by construction. The lite version implements single-quantile linear fitting.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Ordinary least squares, closed-form normal equations; runs in O(n) to fit n points.
- Honest scaling limit: The closed-form fit is O(n) and single-feature; multi-feature regression would need matrix routines.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Quantile Regression (Lite) linear regression in pure Python implementing closed-form least squares on seeded synthetic data; demo recovers known coefficients and reports R^2 with a prediction table.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why generate data with a known line?

**A:** Because the demo knows the ground truth, it can print true vs fitted coefficients side by side, making the fit quality immediately checkable.

**Q:** Does the fit iterate?

**A:** No; the closed-form solution needs no iteration and converges exactly in one pass.

**Q:** How is fit quality reported?

**A:** R^2, the fraction of variance explained, plus a residual column in the prediction table.
