from graph.zero_one_matrix import update_matrix


def test_zero_one_matrix():

    input0 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    res = update_matrix(input0)
    print(res)
    assert res == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    input1 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]

    res = update_matrix(input1)
    print(res)
    assert res == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]