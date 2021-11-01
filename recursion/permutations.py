
# O(n ^ 2 * n!) time |  O(n * n!) space
def getPermutations(array):
    res = []
    backtrack(array, 0, [], res)
    return res

def backtrack(array, idx, ans, res):
    if len(array) == 0:
        res.append(ans.copy())
        return

    for i in range(len(array)):
        rem = array[:i] + array[i + 1:]
        backtrack(rem, idx + 1, ans + [array[i]], res)


# O(n * n!) time | O(n * n!) space
def getPermutations1(array):
    res = []
    backtrack1(array, 0, res)
    return res

def backtrack1(array, idx, res):
    if idx == len(array):
        res.append(array.copy())
        return

    for i in range(idx, len(array)):
        swap(array, i, idx)
        backtrack1(array, idx + 1, res)
        swap(array, i, idx)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    perms = getPermutations([1, 2, 3])
    print(perms)
    assert len(perms) == 6
    assert [1, 2, 3] in perms
    assert [1, 3, 2] in perms
    assert [2, 1, 3] in perms
    assert [2, 3, 1] in perms
    assert [3, 1, 2] in perms
    assert [3, 2, 1] in perms

    perms1 = getPermutations1([1, 2, 3])
    print(perms1)
    assert len(perms1) == 6
    assert [1, 2, 3] in perms1
    assert [1, 3, 2] in perms1
    assert [2, 1, 3] in perms1
    assert [2, 3, 1] in perms1
    assert [3, 1, 2] in perms1
    assert [3, 2, 1] in perms1
