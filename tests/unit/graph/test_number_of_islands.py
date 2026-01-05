from graph.number_of_islands import number_of_island


def test_number_of_islands():
    matrix = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    expected = 3

    actual = number_of_island(matrix)
    print(actual)
    assert actual == expected