
# O(n ^ 4) time | O(n ^ 2) space
def fourNumberSum(array, targetSum):
    if array is None or len(array) == 0:
        return []

    res = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                for z in range(k + 1, len(array)):
                    if array[i] + array[j] + array[k] + array[z] == targetSum:
                        res.append([array[i], array[j], array[k], array[z]])
    return res


# Worst: O(n ^ 3) time | O(n ^ 2) space
# Avg: O(n ^ 2) time | O(n ^ 2) space
def fourNumberSum1(array, targetSum):
    if array is None or len(array) == 0:
        return []

    allPairSums = {}
    res = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            compensate = targetSum - array[i] - array[j]
            if compensate in allPairSums:
                for (x, y) in allPairSums[compensate]:
                    res.append([array[i], array[j], x, y])

        for k in range(0, i):
            sum = array[k] + array[i]
            if sum in allPairSums:
                allPairSums[sum].append((array[i], array[k]))
            else:
                allPairSums[sum] = [(array[i], array[k])]

    return res


def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))


if __name__ == '__main__':
    output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
    print(output)
    output = list(map(sortAndStringify, output))
    quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
    assert len(output) == 2
    for quadruplet in quadruplets:
        assert sortAndStringify(quadruplet) in output

    output = fourNumberSum1([7, 6, 4, -1, 1, 2], 16)
    print(output)
    output = list(map(sortAndStringify, output))
    quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
    assert len(output) == 2
    for quadruplet in quadruplets:
        assert sortAndStringify(quadruplet) in output
