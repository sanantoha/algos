from graph.two_colorable import twoColorable


def test_two_colorable_case1():
    input = [
        [1, 2, 3],
        [0, 2],
        [0, 1],
        [0]
    ]
    actual = twoColorable(input)
    print(actual)
    assert not actual


def test_two_colorable_case2():
    input = [
        [2],
        [2, 3],
        [0, 1],
        [1]
    ]

    actual = twoColorable(input)
    print(actual)
    assert actual