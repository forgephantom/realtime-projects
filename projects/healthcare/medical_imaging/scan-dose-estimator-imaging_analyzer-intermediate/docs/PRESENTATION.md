# Presentation Guide — Scan Dose Estimator: Imaging_Analyzer

## 60-Second Pitch

I built a Scan Dose Estimator that synthesizes a scan, thresholds out the anomaly, and measures its centroid and size. CT dose indices combine tube voltage, tube current-time product, pitch, and scan length into estimates of patient exposure.

Scan Dose Estimator in two sentences: CT dose indices combine tube voltage, tube current-time product, pitch, and scan length into estimates of patient exposure. Lowering dose reduces image quality, so protocols balance diagnostic need against the ALARA principle of keeping exposure as low as reasonably achievable. An estimator lets protocol designers explore that trade-off numerically.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded gaussian background plus a gaussian anomaly blob; threshold at mean + 2 sigma; BFS connected components to isolate and measure the blob.; runs in O(N^2) for an N x N scan: generation, stats, thresholding, and BFS are each linear in pixels..
- Honest scaling limit: Pixel loops suit demo resolutions; megapixel scans would want numpy or tiled processing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Scan Dose Estimator in Python with synthetic scan generation, threshold segmentation, and connected-component blob measurement.
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
