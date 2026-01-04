from algo_math.custom_pow import calc_pow


def test_pow_case1():
    assert calc_pow(4, 2) == 16

def test_pow_case2():
    assert calc_pow(2, 4) == 16


def test_pow_case3():
    assert calc_pow(2.0, -2) == 0.25


def test_pow_case4():
    assert calc_pow(2.1, 3) == 9.261000000000001