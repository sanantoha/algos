from dynamic.knapsack_problem import knapsack_problem


def test_knapsack_problem():
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    expected = [10, [1, 3]]
    actual = knapsack_problem(items, capacity)
    print(actual)
    assert actual == expected