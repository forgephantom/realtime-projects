# Presentation Guide — Symptom Checker Flow: Decision Tree Classifier

## 60-Second Pitch

A Symptom Checker Flow decision tree in pure Python that learns greedy Gini splits from seeded data and shows its reasoning as a printable tree. Symptom checkers map reported symptoms to possible conditions using probabilistic reasoning, then recommend a care setting rather than a diagnosis.

Symptom Checker Flow in two sentences: Symptom checkers map reported symptoms to possible conditions using probabilistic reasoning, then recommend a care setting rather than a diagnosis. The flow must handle vague inputs gracefully and always offer an escalation path. Synthetic symptom sets with known intended routing validate the flow logic.

## Architecture Talking Points

- Components: `DecisionTree` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Greedy binary splits maximizing Gini impurity gain; runs in O(d * n^2) worst case to find splits for d features, n rows.
- Honest scaling limit: Exhaustive split search is O(n^2)-ish per level, so the demo stays at a few hundred rows; larger data needs histogram or approximate splits.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Symptom Checker Flow decision tree classifier in pure Python using greedy Gini-impurity splits; demo prints the learned tree as text and reports test accuracy on a held-out split.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are splits chosen?

**A:** The best (feature, threshold) pair is the one maximizing impurity gain, evaluated exhaustively over observed feature values.

**Q:** What stops the tree from growing forever?

**A:** --max-depth caps recursion; pure or unsplittable nodes also stop early as majority-class leaves.

**Q:** How is the tree displayed?

**A:** print_tree walks the nested dict nodes and indents each level, so the whole model is human-readable.
