
# O(n ^ 2) time | O(1) space
def subarraySort(array):
    if array is None or len(array) == 0:
        return [-1, -1]

    start = float('inf')
    end = -1

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] > array[i]:
                start = min(start, j)
                end = i
                break
    return [start, end]


# O(n) time | O(1) space
def subarraySort1(array):
    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(num, minOutOfOrder)
            maxOutOfOrder = max(num, maxOutOfOrder)

    if minOutOfOrder == float('inf'):
        return [-1, -1]

    l = 0
    while minOutOfOrder >= array[l]:
        l += 1

    r = len(array) - 1
    while maxOutOfOrder <= array[r]:
        r -= 1

    return [l, r]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return num > array[i + 1] or num < array[i - 1]


if __name__ == '__main__':
    actual = subarraySort1([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(actual)
    # assert actual == [3, 9]

    actual = subarraySort1([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19])
    print(actual)
    # assert actual == [4, 9]