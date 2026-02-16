# robust-dvrp

Reproducible toy baseline for a (future) robust dynamic VRP project.
This public repo intentionally contains **only a safe baseline** (no unpublished research logic).

## Quickstart

```bash
python -m pip install -e ".[dev]"
python -m robust_dvrp.cli --n 80 --k 7 --seed 0
pytest -q
