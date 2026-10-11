# Presentation Guide — TAM SAM SOM Estimator: Swot_Analyzer

## 60-Second Pitch

I built a TAM SAM SOM Estimator that scores SWOT quadrants and turns the top factors into concrete TOWS actions. TAM is everyone who could ever buy, SAM is the slice you can actually reach, and SOM is the share you can realistically win.

TAM SAM SOM Estimator in two sentences: TAM is everyone who could ever buy, SAM is the slice you can actually reach, and SOM is the share you can realistically win. Each layer needs its own math: top-down from industry figures or bottom-up from customer counts times price. The discipline is documenting every assumption so the number can be challenged.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Weighted scoring per SWOT quadrant (sum of weight x score), then TOWS pairing of top factors into SO/WO/ST/WT actions.; runs in O(F) over F factors; sorting for top factors is O(F log F)..
- Honest scaling limit: The math is trivial at any factor count; real use is in workshop facilitation, not computation.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a TAM SAM SOM Estimator in Python with weighted SWOT quadrant scoring and TOWS action-item generation.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is a quadrant scored?

**A:** Each factor gets a weight and a 1-5 impact score; the quadrant total is the sum of weight times score.

**Q:** What does dominant mean?

**A:** The highest-scoring quadrant is the dominant one; the matrix also shows whether internal or external factors lead.

**Q:** What are TOWS actions?

**A:** Strengths with Opportunities, Weaknesses with Opportunities, Strengths with Threats, Weaknesses with Threats.
