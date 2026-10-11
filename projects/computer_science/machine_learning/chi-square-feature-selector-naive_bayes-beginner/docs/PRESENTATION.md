# Presentation Guide — Chi-Square Feature Selector: Naive Bayes Classifier

## 60-Second Pitch

A Chi-Square Feature Selector Naive Bayes classifier in pure Python that learns Gaussian feature likelihoods from seeded data and proves itself with a confusion matrix. The chi-square test scores categorical features by independence from the target: high scores mean strong association.

Chi-Square Feature Selector in two sentences: The chi-square test scores categorical features by independence from the target: high scores mean strong association. It is fast, univariate, and the classic filter for text classification feature selection. SelectKBest keeps the top scorers.

## Architecture Talking Points

- Components: `GaussianNB` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Gaussian Naive Bayes with log-space scoring; runs in O(n*d) to fit n samples with d features; O(c*d) per prediction.
- Honest scaling limit: Pure-Python loops over features make this fine for thousands of samples; larger or high-dimensional data would want vectorization.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Chi-Square Feature Selector Naive Bayes classifier in pure Python with Gaussian likelihoods and log-space scoring; demo trains on seeded synthetic data and reports accuracy with a confusion matrix.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Does it use log probabilities?

**A:** Yes; scores are accumulated in log space, which avoids underflow when multiplying many small probabilities.

**Q:** What features does the demo use?

**A:** The demo uses two Gaussian blobs per class in two dimensions, but the classifier itself works for any feature count.

**Q:** How is the test set made?

**A:** --train-frac controls the split; the default 0.7 keeps 30 percent of samples for testing.
