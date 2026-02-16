# robust-dvrp

Reproducible toy baseline for a (future) robust dynamic VRP project.
This public repo intentionally contains **only a safe baseline** (no unpublished research logic).

## Quickstart

```bash
python -m pip install -e ".[dev]"
python -m robust_dvrp.cli --n 80 --k 7 --seed 0
pytest -q
```

## What's inside

- `src/robust_dvrp/vrp.py`: toy solver (angle partition + nearest neighbor)
- `src/robust_dvrp/cli.py`: CLI entrypoint
- `tests/`: pytest tests
- `.github/workflows/ci.yml`: GitHub Actions CI

## Roadmap

- [ ] Add benchmark scripts and report (runtime / distance vs baselines)
- [ ] Add more heuristics (2-opt, savings, local search)
- [ ] (Private) research-grade robust / dynamic extensions
