# O(n) time | O(1) space
def threeNumberSort(arr, ord):
    if not arr:
        return []

    cnt = [0, 0, 0]
    for num in arr:
        for i, v in enumerate(ord):
            if num == v:
                cnt[i] += 1


    idx = 0
    for i, v in enumerate(ord):
        for _ in range(cnt[i]):
            arr[idx] = v
            idx += 1

    return arr


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