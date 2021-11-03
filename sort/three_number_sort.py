# O(n) time | O(1) space
def threeNumberSort(array, order):
    fst = 0
    snd = 0
    thrd = 0
    for num in array:
        if order[0] == num:
            fst += 1
        elif order[1] == num:
            snd += 1
        else:
            thrd += 1

    idx = 0
    idx = fillArr(array, idx, fst, order[0])
    idx = fillArr(array, idx, snd, order[1])
    fillArr(array, idx, thrd, order[2])
    return array


def fillArr(array, idx, count, value):
    while count > 0:
        array[idx] = value
        idx += 1
        count -= 1
    return idx


# O(n) time | O(1) space
def threeNumberSort1(array, order):

    l = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            array[i], array[l] = array[l], array[i]
            l += 1

    r = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] == order[2]:
            array[i], array[r] = array[r], array[i]
            r -= 1

    return array


if __name__ == '__main__':
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    expected = [0, 0, 0, 1, 1, 1, -1, -1]

    actual = threeNumberSort(array, order)
    print(actual)
    assert actual == expected

    actual = threeNumberSort1(array, order)
    print(actual)
    assert actual == expected