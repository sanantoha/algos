
# O(n ^ 2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    if array is None or len(array) == 0:
        return []

    maxSumIncSubseq = array.copy()
    prev = [None] * len(array)

    maxSum = float('-inf')
    maxIdx = 0

    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i] and maxSumIncSubseq[i] < maxSumIncSubseq[j] + array[i]:
                maxSumIncSubseq[i] = maxSumIncSubseq[j] + array[i]
                prev[i] = j

        if maxSum < maxSumIncSubseq[i]:
            maxSum = maxSumIncSubseq[i]
            maxIdx = i

    res = []
    idx = maxIdx
    while idx is not None:
        val = array[idx]
        res.append(val)
        idx = prev[idx]
    res.reverse()
    return [maxSum, res]


if __name__ == '__main__':
    input = [-1, 1]
    expected = [1, [1]]

    actual = maxSumIncreasingSubsequence(input)
    print(actual)
    assert actual == expected


    input = [10, 70, 20, 30, 50, 11, 30]
    expected = [110, [10, 20, 30, 50]]

    actual = maxSumIncreasingSubsequence(input)
    print(actual)
    assert actual == expected


    input = [8, 12, 2, 3, 15, 5, 7]
    expected = [35, [8, 12, 15]]

    actual = maxSumIncreasingSubsequence(input)
    print(actual)
    assert actual == expected


    input = [-5, -4, -3, -2, -1]

    expected = [-1, [-1]]

    actual = maxSumIncreasingSubsequence(input)
    print(actual)
    assert actual == expected