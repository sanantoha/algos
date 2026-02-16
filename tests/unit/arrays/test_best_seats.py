from arrays.best_seats import bestSeat


def test_best_seats_case1():
    actual = bestSeat([1, 0, 1, 0, 0, 0, 1])
    assert actual == 4


def test_best_seats_case2():
    actual = bestSeat([1])
    assert actual == -1


def test_best_seats_case3():
    actual = bestSeat([1, 0, 1])
    assert actual == 1


def test_best_seats_case4():
    actual = bestSeat([1, 0, 0, 1])
    assert actual == 1


def test_best_seats_case5():
    actual = bestSeat([1, 1, 1])
    assert actual == -1


def test_best_seats_case6():
    actual = bestSeat([1, 0, 0, 1, 0, 0, 1])
    assert actual == 1


def test_best_seats_case7():
    actual = bestSeat([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    assert actual == 3

