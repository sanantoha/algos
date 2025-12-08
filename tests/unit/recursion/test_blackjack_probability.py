from recursion.blackjack_probability import blackjackProbability


def test_blakjack_probability_case1():
    actual = blackjackProbability(21, 15)
    print(actual)
    assert actual == 0.45


def test_blakjack_probability_case2():
    actual = blackjackProbability(21, 21)
    print(actual)
    assert actual == 0


def test_blakjack_probability_case3():
    actual = blackjackProbability(21, 20)
    print(actual)
    assert actual == 0


def test_blakjack_probability_case4():
    actual = blackjackProbability(21, 17)
    print(actual)
    assert actual == 0


def test_blakjack_probability_case5():
    actual = blackjackProbability(21, 12)
    print(actual)
    assert actual == 0.268


def test_blakjack_probability_case6():
    actual = blackjackProbability(21, 5)
    print(actual)
    assert actual == 0.295


def test_blakjack_probability_case7():
    actual = blackjackProbability(30, 25)
    print(actual)
    assert actual == 0.5