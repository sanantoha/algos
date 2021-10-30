
# O(n * 2 ^ n) time | O(n * 2 ^ n) space
def powerset(array):
    return powerset_rec(array, len(array) - 1)


def powerset_rec(array, idx):
    if idx < 0:
        return [[]]

    elem = array[idx]

    sub_res = powerset_rec(array, idx - 1)
    sub_res_len = len(sub_res)
    for i in range(sub_res_len):
        lst = sub_res[i].copy()
        lst.append(elem)
        sub_res.append(lst)

    return sub_res


# O(n * 2 ^ n) time | O(n * 2 ^ n) space
def powerset1(array):
    res = [[]]

    for num in array:
        sub_res = []
        for lst in res:
            nlst = lst.copy()
            nlst.append(num)
            sub_res.append(nlst)
        res.extend(sub_res)

    return res


if __name__ == '__main__':
    print(powerset([1, 2, 3]))
    print(powerset1([1, 2, 3]))
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