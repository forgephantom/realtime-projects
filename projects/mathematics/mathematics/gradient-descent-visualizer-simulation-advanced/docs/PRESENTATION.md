# Presentation Guide — Gradient Descent Visualizer: Simulation (Logistic Growth)

## 60-Second Pitch

A Gradient Descent Visualizer simulation in pure Python that integrates logistic growth with Euler steps and prints the full trajectory toward carrying capacity. Gradient descent minimizes a function by stepping opposite the gradient, with the learning rate controlling the trade-off between speed and oscillation.

Gradient Descent Visualizer in two sentences: Gradient descent minimizes a function by stepping opposite the gradient, with the learning rate controlling the trade-off between speed and oscillation. On convex quadratics it converges linearly; on ravines it zigzags unless the rate is tuned. The visualizer traces the path on 2D surfaces and exports the trajectory.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Explicit Euler integration of logistic growth; runs in O(steps).
- Honest scaling limit: The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Gradient Descent Visualizer simulator in Python (stdlib) implementing Euler integration of logistic growth with seeded parameters; demo runs end-to-end and prints the trajectory table with summary statistics.
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
