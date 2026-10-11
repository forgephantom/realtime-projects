# Presentation Guide — Polynomial Feature Expansion: Linear Regression

## 60-Second Pitch

A Polynomial Feature Expansion linear regression in pure Python that generates noisy data with a known line, recovers it with closed-form least squares, and shows the fit quality with R^2. Linear models can fit curves if you first expand features into polynomial terms: x becomes [x, x^2, x^3], and OLS fits the rest.

Polynomial Feature Expansion in two sentences: Linear models can fit curves if you first expand features into polynomial terms: x becomes [x, x^2, x^3], and OLS fits the rest. Degree controls flexibility, and high degrees overfit wildly without regularization. It is the simplest way to see the bias-variance trade-off in action.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Ordinary least squares, closed-form normal equations; runs in O(n) to fit n points.
- Honest scaling limit: The closed-form fit is O(n) and single-feature; multi-feature regression would need matrix routines.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Polynomial Feature Expansion linear regression in pure Python implementing closed-form least squares on seeded synthetic data; demo recovers known coefficients and reports R^2 with a prediction table.
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
