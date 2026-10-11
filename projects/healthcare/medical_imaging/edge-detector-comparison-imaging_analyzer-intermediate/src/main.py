#!/usr/bin/env python3
"""Edge Detector Comparison: Imaging_Analyzer.

Sobel and Prewitt use small gradient kernels while Canny chains Gaussian smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding into cleaner edges. Each detector trades sensitivity against false positives differently under noise. Benchmarking precision and recall on phantoms with annotated true edges makes the trade-off concrete.

Demo dataset idea: Generates phantoms with annotated true edges for detector benchmarking..
"""

import argparse
import math
import random
import statistics
from collections import deque

SLUG = "imaging-analyzer"
PARAMS = {'detector_list': 'which detectors to compare', 'noise_level': 'noise added to the phantom', 'edge_count': 'number of true edges in the phantom', 'seed': 'random seed for phantom generation'}

SHADES = " .:-=+*#%@"


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def _param(key, default):
    """Read a project param defensively; coerce descriptive text to the default's type."""
    v = PARAMS.get(key, default) if isinstance(PARAMS, dict) else default
    if isinstance(default, bool):
        return v if isinstance(v, bool) else default
    if isinstance(default, (int, float)) and not isinstance(v, (int, float)):
        return _num(v, default)
    return v


def generate_scan(seed: int, size: int = 24) -> tuple:
    """Seeded NxN scan: gaussian background plus a gaussian anomaly blob."""
    rng = random.Random(seed)
    cx = rng.randint(size // 3, 2 * size // 3)
    cy = rng.randint(size // 3, 2 * size // 3)
    sigma, amplitude = 2.5, 120.0
    grid = []
    for y in range(size):
        row = []
        for x in range(size):
            dist2 = (x - cx) ** 2 + (y - cy) ** 2
            blob = amplitude * math.exp(-dist2 / (2.0 * sigma ** 2))
            row.append(rng.gauss(50.0, 8.0) + blob)
        grid.append(row)
    return grid, (cx, cy)


def region_stats(grid: list) -> dict:
    """Mean, stdev, min, and max over the whole scan."""
    flat = [v for row in grid for v in row]
    return {"mean": statistics.mean(flat),
            "stdev": statistics.pstdev(flat),
            "min": min(flat), "max": max(flat),
            "pixels": len(flat)}


def segment(grid: list, threshold: float) -> list:
    """Binary mask of pixels above the threshold."""
    return [[1 if v > threshold else 0 for v in row] for row in grid]


def connected_components(mask: list) -> list:
    """BFS connected components (4-neighborhood) of the mask."""
    size = len(mask)
    seen = [[False] * size for _ in range(size)]
    components = []
    for y in range(size):
        for x in range(size):
            if mask[y][x] and not seen[y][x]:
                comp, queue = [], deque([(x, y)])
                seen[y][x] = True
                while queue:
                    px, py = queue.popleft()
                    comp.append((px, py))
                    for nx, ny in ((px + 1, py), (px - 1, py),
                                   (px, py + 1), (px, py - 1)):
                        if (0 <= nx < size and 0 <= ny < size
                                and mask[ny][nx] and not seen[ny][nx]):
                            seen[ny][nx] = True
                            queue.append((nx, ny))
                components.append(comp)
    return components


def largest_blob(components: list) -> dict:
    """Centroid, pixel count, and bbox of the largest component."""
    if not components:
        return {"found": False}
    comp = max(components, key=len)
    xs = [p[0] for p in comp]
    ys = [p[1] for p in comp]
    return {"found": True,
            "pixel_count": len(comp),
            "centroid": (sum(xs) / len(xs), sum(ys) / len(ys)),
            "bbox": (min(xs), min(ys), max(xs), max(ys))}


def render_ascii(grid: list, mask: list) -> str:
    """ASCII heatmap of the scan with the segmented blob marked."""
    flat = [v for row in grid for v in row]
    lo, hi = min(flat), max(flat)
    span = hi - lo if hi > lo else 1.0
    lines = []
    for y, row in enumerate(grid):
        chars = []
        for x, v in enumerate(row):
            if mask[y][x]:
                chars.append("#")
            else:
                chars.append(SHADES[int((v - lo) / span
                                        * (len(SHADES) - 1))])
            chars.append(" ")
        lines.append("".join(chars).rstrip())
    return "\n".join(lines)


def run_demo(seed: int) -> int:
    """Seeded demo: stats, segmentation, blob report, ASCII map."""
    size = _param("size", 24)
    grid, true_center = generate_scan(seed, size=size)
    stats = region_stats(grid)
    threshold = stats["mean"] + 2.0 * stats["stdev"]
    mask = segment(grid, threshold)
    components = connected_components(mask)
    blob = largest_blob(components)
    print("Edge Detector Comparison: Imaging_Analyzer  (topic: Edge Detector Comparison, seed=%d)" % seed)
    print("Scan: %dx%d (%d px), true anomaly center: %s"
          % (size, size, stats["pixels"], true_center))
    print("Region stats: mean=%.2f stdev=%.2f min=%.2f max=%.2f"
          % (stats["mean"], stats["stdev"], stats["min"], stats["max"]))
    print("Threshold (mean + 2*stdev): %.2f" % threshold)
    print("Above-threshold components: %d" % len(components))
    if blob["found"]:
        cx, cy = blob["centroid"]
        tx, ty = true_center
        err = math.hypot(cx - tx, cy - ty)
        print("Largest blob: %d px, centroid=(%.2f, %.2f), "
              "bbox=%s" % (blob["pixel_count"], cx, cy, blob["bbox"]))
        print("Detection error vs true center: %.2f px" % err)
    else:
        print("No anomaly found above threshold.")
    print("\nScan map (# = segmented blob):")
    print(render_ascii(grid, mask))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Edge Detector Comparison: Imaging_Analyzer: Sobel and Prewitt use small gradient kernels while Canny chains Gaussian smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding into cleaner edges. Each detector trades sensitivity against false positives differently under noise. Benchmarking precision and recall on phantoms with annotated true edges makes the trade-off concrete."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--size", type=int, default=None,
                        help="Scan resolution in pixels (overrides params).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded scan analyzer demo."""
    args = build_parser().parse_args(argv)
    if args.size is not None and isinstance(PARAMS, dict):
        PARAMS["size"] = args.size
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
