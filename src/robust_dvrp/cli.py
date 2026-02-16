from __future__ import annotations

import argparse
from .vrp import generate_instance, solve_nearest_neighbor, validate_solution


def main() -> int:
    p = argparse.ArgumentParser(description="Toy baseline robust-dvrp (demo).")
    p.add_argument("--n", type=int, default=50, help="number of customers")
    p.add_argument("--k", type=int, default=5, help="number of vehicles")
    p.add_argument("--seed", type=int, default=0, help="random seed (deterministic)")
    args = p.parse_args()

    pts = generate_instance(n=args.n, seed=args.seed)
    sol = solve_nearest_neighbor(points=pts, k=args.k, seed=args.seed)
    validate_solution(args.n, sol)

    print(f"n={args.n}, k={args.k}, seed={args.seed}")
    print(f"total_distance={sol.total_distance:.6f}")
    for i, r in enumerate(sol.routes):
        print(f"route[{i}] len={len(r)}: {r[:10]}{' ...' if len(r) > 10 else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
