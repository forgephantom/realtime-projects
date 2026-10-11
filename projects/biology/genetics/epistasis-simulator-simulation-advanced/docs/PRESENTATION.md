# Presentation Guide — Epistasis Ratio Simulator: Simulation (Logistic Growth)

## 60-Second Pitch

A Epistasis Ratio Simulator simulation in pure Python that integrates logistic growth with Euler steps and prints the full trajectory toward carrying capacity. Epistasis means one gene masks or modifies another, producing ratios like 9:7 (complementary), 12:3:1 (dominant epistasis), or 9:3:4 (recessive epistasis) instead of 9:3:3:1.

Epistasis Ratio Simulator in two sentences: Epistasis means one gene masks or modifies another, producing ratios like 9:7 (complementary), 12:3:1 (dominant epistasis), or 9:3:4 (recessive epistasis) instead of 9:3:3:1. The simulator generates offspring under each epistatic model and fits observed counts to identify the interaction type. It explains the deviating phenotypic classes.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Explicit Euler integration of logistic growth; runs in O(steps).
- Honest scaling limit: The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Epistasis Ratio Simulator simulator in Python (stdlib) implementing Euler integration of logistic growth with seeded parameters; demo runs end-to-end and prints the trajectory table with summary statistics.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What dynamics does the model show?

**A:** Logistic growth: fast early rise that levels off at the carrying capacity K, a common shape for adoption and saturation processes.

**Q:** How is accuracy controlled?

**A:** --steps and --dt; smaller dt is more accurate, larger dt runs faster but can overshoot.

**Q:** Why Euler instead of RK4?

**A:** Euler is first-order and simple to read; the template favors clarity over the accuracy of higher-order integrators.
