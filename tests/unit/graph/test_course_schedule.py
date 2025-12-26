from graph.course_schedule import can_finish, can_finish_kahn_algorithm


def test_can_finish():
    assert can_finish(1, []) is True

    assert can_finish(2, [[1, 0]]) is True

    assert not can_finish(2, [[1, 0], [0, 1]])

    assert not can_finish(4, [[1, 0], [2, 1], [3, 2], [0, 3]])

    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True


def test_can_finish_kahn_algorithm():
    assert can_finish_kahn_algorithm(1, []) is True

    assert can_finish_kahn_algorithm(2, [[1, 0]]) is True

    assert not can_finish_kahn_algorithm(2, [[1, 0], [0, 1]])

    assert not can_finish_kahn_algorithm(4, [[1, 0], [2, 1], [3, 2], [0, 3]])

    assert can_finish_kahn_algorithm(4, [[1, 0], [2, 1], [3, 2]]) is True