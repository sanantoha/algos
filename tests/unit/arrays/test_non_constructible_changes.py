from arrays.non_constructible_changes import non_constructible_changes


def test_non_constructible_changes():
    coins = [5, 7, 1, 1, 2, 3, 22]
    res = non_constructible_changes(coins)
    print(res)
    assert res == 20