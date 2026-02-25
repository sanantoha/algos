from graph.single_cycle_check import single_cycle_check


def test_single_cycle_check():
    array = [2, 3, 1, -4, -4, 2]
    print(single_cycle_check(array))
    assert single_cycle_check(array)