from recursion.permutations import getPermutations, getPermutations1


def test_permutations():
    perms = getPermutations([1, 2, 3])
    print(perms)
    assert len(perms) == 6
    assert [1, 2, 3] in perms
    assert [1, 3, 2] in perms
    assert [2, 1, 3] in perms
    assert [2, 3, 1] in perms
    assert [3, 1, 2] in perms
    assert [3, 2, 1] in perms


def test_permutations_rec():
    perms1 = getPermutations1([1, 2, 3])
    print(perms1)
    assert len(perms1) == 6
    assert [1, 2, 3] in perms1
    assert [1, 3, 2] in perms1
    assert [2, 1, 3] in perms1
    assert [2, 3, 1] in perms1
    assert [3, 1, 2] in perms1
    assert [3, 2, 1] in perms1