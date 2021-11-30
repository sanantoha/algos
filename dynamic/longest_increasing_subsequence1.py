
# O(n ^ 2) time | O(n) space
def longestIncreasingSubsequence(arr):
    if arr is None or len(arr) == 0:
        return []

    lengths = [1] * len(arr)
    prev = [-1] * len(arr)

    max = float('-inf')
    maxIdx = 0

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j

        if max < lengths[i]:
            max = lengths[i]
            maxIdx = i

    return buildList(arr, prev, maxIdx)


# O(n * log(n)) time | O(n) space
def longestIncreasingSubsequence1(arr):
    if arr is None or len(arr) == 0:
        return []

    indices = [-1] * (len(arr) + 1)
    prev = [-1] * len(arr)

    length = 0

    for i in range(len(arr)):
        newLength = binarySearch(arr, indices, 1, length, arr[i])
        prev[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)

    return buildList(arr, prev, indices[length])


def binarySearch(arr, indices, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if target < arr[indices[mid]]:
            r = mid - 1
        else:
            l = mid + 1

    return l



def buildList(arr, prev, maxIdx):
    res = []
    currIdx = maxIdx
    while currIdx >= 0:
        res.append(arr[currIdx])
        currIdx = prev[currIdx]

    res.reverse()
    return res


if __name__ == '__main__':
    input = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
    expected = [-24, 2, 3, 5, 6, 35]

    actual = longestIncreasingSubsequence(input)
    print(actual)
    assert actual == expected

    actual = longestIncreasingSubsequence1(input)
    print(actual)
    assert actual == expected
