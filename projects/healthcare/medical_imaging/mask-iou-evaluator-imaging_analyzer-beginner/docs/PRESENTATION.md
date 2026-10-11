# Presentation Guide — Mask IoU Evaluator: Imaging_Analyzer

## 60-Second Pitch

I built a Mask IoU Evaluator that synthesizes a scan, thresholds out the anomaly, and measures its centroid and size. Intersection over Union and the Dice coefficient are the standard ways to compare a predicted segmentation mask against ground truth, ranging from zero for no overlap to one for perfect agreement.

Mask IoU Evaluator in two sentences: Intersection over Union and the Dice coefficient are the standard ways to compare a predicted segmentation mask against ground truth, ranging from zero for no overlap to one for perfect agreement. Per-class scores reveal which structures a model segments well and which it misses. Tracking these metrics across experiments is how segmentation quality is actually managed.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded gaussian background plus a gaussian anomaly blob; threshold at mean + 2 sigma; BFS connected components to isolate and measure the blob.; runs in O(N^2) for an N x N scan: generation, stats, thresholding, and BFS are each linear in pixels..
- Honest scaling limit: Pixel loops suit demo resolutions; megapixel scans would want numpy or tiled processing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Mask IoU Evaluator in Python with synthetic scan generation, threshold segmentation, and connected-component blob measurement.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is the threshold chosen?

**A:** Mean plus two standard deviations of the whole scan; the bright anomaly sits well above background noise.

**Q:** How is the blob isolated?

**A:** Breadth-first search over 4-connected above-threshold pixels; the largest component is reported as the anomaly.

**Q:** What if the blob is faint?

**A:** A brighter or larger blob segments cleanly; a faint one near the noise floor may split or vanish, which the report shows.
