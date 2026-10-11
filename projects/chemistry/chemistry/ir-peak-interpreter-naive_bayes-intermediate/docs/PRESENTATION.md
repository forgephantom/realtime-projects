# Presentation Guide — IR Peak Interpreter: Naive Bayes Classifier

## 60-Second Pitch

A IR Peak Interpreter Naive Bayes classifier in pure Python that learns Gaussian feature likelihoods from seeded data and proves itself with a confusion matrix. Infrared absorption peaks correspond to vibrating bonds, so a broad band near 3300 reciprocal centimeters suggests O-H or N-H while a sharp peak near 1700 suggests a carbonyl.

IR Peak Interpreter in two sentences: Infrared absorption peaks correspond to vibrating bonds, so a broad band near 3300 reciprocal centimeters suggests O-H or N-H while a sharp peak near 1700 suggests a carbonyl. The interpreter classifies functional groups from peak lists using learned patterns.

## Architecture Talking Points

- Components: `GaussianNB` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Gaussian Naive Bayes with log-space scoring; runs in O(n*d) to fit n samples with d features; O(c*d) per prediction.
- Honest scaling limit: Pure-Python loops over features make this fine for thousands of samples; larger or high-dimensional data would want vectorization.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a IR Peak Interpreter Naive Bayes classifier in pure Python with Gaussian likelihoods and log-space scoring; demo trains on seeded synthetic data and reports accuracy with a confusion matrix.
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
