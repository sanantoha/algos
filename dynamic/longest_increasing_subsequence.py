
# O(n ^ 2) time | O(n) space
def longestIncreasingSubsequence(array):
    if array is None or len(array) == 0:
        return []

    lengths = [1 for _ in array]
    prev = [None for _ in array]
    maxIdx = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j

        if lengths[i] > lengths[maxIdx]:
            maxIdx = i

    return buildSequence(array, prev, maxIdx)


def buildSequence(array, prev, idx):
    sequence = []
    while idx is not None:
        sequence.append(array[idx])
        idx = prev[idx]

    return list(reversed(sequence))


# O(n * log(n)) time | O(n) space
def longestIncreasingSubsequence1(arr):
    if arr is None or len(arr) == 0:
        return []

    indices = [None for _ in range(len(arr) + 1)]
    prev = [None for _ in arr]
    length = 0

    for i in range(len(arr)):
        newLength = binarySearch(arr, indices, 1, length, arr[i])
        prev[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)

    return buildSequence(arr, prev, indices[length])


def binarySearch(arr, indices, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[indices[mid]] < target:
            l = mid + 1
        else:
            r = mid - 1

    return l


if __name__ == '__main__':
    input = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

    actual = longestIncreasingSubsequence(input)
    print(actual)
    assert actual == [-24, 2, 3, 5, 6, 35]

    actual = longestIncreasingSubsequence1(input)
    print(actual)
    assert actual == [-24, 2, 3, 5, 6, 35]