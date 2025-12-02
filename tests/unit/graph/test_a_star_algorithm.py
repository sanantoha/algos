from graph.a_star_algorithm import a_star_algorithm


def test_a_star_algorithm():
    start_row = 0
    start_col = 1
    end_row = 4
    end_col = 3
    graph = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 0, 0, 0]]
    expected = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
    actual = a_star_algorithm(start_row, start_col, end_row, end_col, graph)
    print(actual)
    assert actual == expected