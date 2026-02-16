from robust_dvrp.vrp import generate_instance, solve_nearest_neighbor, validate_solution


def test_solution_visits_each_customer_exactly_once():
    n, k, seed = 80, 7, 123
    pts = generate_instance(n=n, seed=seed)
    sol = solve_nearest_neighbor(points=pts, k=k, seed=seed)
    validate_solution(n, sol)


def test_deterministic_given_seed():
    n, k, seed = 60, 6, 0
    pts = generate_instance(n=n, seed=seed)
    a = solve_nearest_neighbor(points=pts, k=k, seed=seed).total_distance
    b = solve_nearest_neighbor(points=pts, k=k, seed=seed).total_distance
    assert a == b
