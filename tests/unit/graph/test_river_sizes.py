from graph.river_sizes import river_sizes

def test_river_sizes_case1():
    test_input = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    expected = [1, 2, 2, 2, 5]

    actual = sorted(river_sizes(test_input))
    print(actual)
    assert actual == expected


def test_river_sizes_case2():
    test_input = [
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    ]

    expected = [1, 1, 2, 2, 5, 21]

    actual = sorted(river_sizes(test_input))
    print(actual)
    assert actual == expected