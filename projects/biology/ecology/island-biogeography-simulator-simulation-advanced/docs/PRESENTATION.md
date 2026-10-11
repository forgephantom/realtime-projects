# Presentation Guide — Island Biogeography Equilibrium Simulator: Simulation (Logistic Growth)

## 60-Second Pitch

A Island Biogeography Equilibrium Simulator simulation in pure Python that integrates logistic growth with Euler steps and prints the full trajectory toward carrying capacity. Island biogeography predicts species richness from island area and isolation: immigration declines as species accumulate while extinction rises, equilibrating where the curves cross.

Island Biogeography Equilibrium Simulator in two sentences: Island biogeography predicts species richness from island area and isolation: immigration declines as species accumulate while extinction rises, equilibrating where the curves cross. Larger, nearer islands hold more species. The simulator computes equilibria across island configurations and plots the immigration-extinction balance.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Explicit Euler integration of logistic growth; runs in O(steps).
- Honest scaling limit: The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Island Biogeography Equilibrium Simulator simulator in Python (stdlib) implementing Euler integration of logistic growth with seeded parameters; demo runs end-to-end and prints the trajectory table with summary statistics.
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
