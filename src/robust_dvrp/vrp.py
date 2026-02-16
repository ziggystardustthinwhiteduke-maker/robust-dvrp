from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import math
import random


Point = Tuple[float, float]


def euclid(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


@dataclass(frozen=True)
class Solution:
    routes: List[List[int]]  # each route is list of customer indices (0..n-1)
    total_distance: float


def generate_instance(n: int, seed: int) -> List[Point]:
    """Generate n customer points in [0,1]^2 (toy instance)."""
    rng = random.Random(seed)
    return [(rng.random(), rng.random()) for _ in range(n)]


def solve_nearest_neighbor(points: List[Point], k: int, seed: int = 0) -> Solution:
    """
    Toy baseline:
      - depot fixed at (0,0)
      - partition customers into k groups by angle around depot
      - within each group, visit by greedy nearest-neighbor
    Not optimal; just deterministic + testable + DS&A-ish baseline.
    """
    if k <= 0:
        raise ValueError("k must be >= 1")
    n = len(points)
    if n == 0:
        return Solution(routes=[[] for _ in range(k)], total_distance=0.0)

    depot: Point = (0.0, 0.0)

    # sort by polar angle (stable deterministic; seed only used for tie-break shuffle if needed)
    idxs = list(range(n))
    rng = random.Random(seed)
    rng.shuffle(idxs)  # tie-breaker randomness (still deterministic with seed)

    idxs.sort(key=lambda i: math.atan2(points[i][1] - depot[1], points[i][0] - depot[0]))

    groups: List[List[int]] = [[] for _ in range(k)]
    for t, i in enumerate(idxs):
        groups[t % k].append(i)

    routes: List[List[int]] = []
    total = 0.0
    for g in groups:
        if not g:
            routes.append([])
            continue

        # nearest-neighbor route starting from depot
        unvisited = set(g)
        route: List[int] = []
        cur = depot
        while unvisited:
            nxt = min(unvisited, key=lambda j: euclid(cur, points[j]))
            unvisited.remove(nxt)
            route.append(nxt)
            total += euclid(cur, points[nxt])
            cur = points[nxt]
        total += euclid(cur, depot)  # return to depot
        routes.append(route)

    return Solution(routes=routes, total_distance=total)


def validate_solution(n: int, sol: Solution) -> None:
    """Raise if solution violates basic constraints (each customer exactly once)."""
    seen = []
    for r in sol.routes:
        seen.extend(r)

    if sorted(seen) != list(range(n)):
        raise ValueError(f"Invalid visit set: expected 0..{n-1}, got {sorted(seen)[:10]} ...")
