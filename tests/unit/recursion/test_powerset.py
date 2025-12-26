from recursion.powerset import powerset, powerset1


def test_powerset():
    output = list(map(lambda x: set(x), powerset([1, 2, 3])))
    assert len(output) == 8
    assert set([]) in output
    assert set([1]) in output
    assert set([2]) in output
    assert set([1, 2]) in output
    assert set([3]) in output
    assert set([1, 3]) in output
    assert set([2, 3]) in output
    assert set([1, 2, 3]) in output


def test_powerset1():
    output = list(map(lambda x: set(x), powerset1([1, 2, 3])))
    assert len(output) == 8
    assert set([]) in output
    assert set([1]) in output
    assert set([2]) in output
    assert set([1, 2]) in output
    assert set([3]) in output
    assert set([1, 3]) in output
    assert set([2, 3]) in output
    assert set([1, 2, 3]) in output