
# O(n ^ 2) time | O(n) space
def diskStacking(disks):
    if disks is None or len(disks) == 0:
        return []

    disks.sort(key=lambda x: x[2])

    heights = [h for _, _, h in disks]
    prev = [None] * len(disks)

    maxHeight = float('-inf')
    maxIdx = 0

    for i in range(len(disks)):
        for j in range(0, i):
            if less(disks[j], disks[i]) and heights[i] < heights[j] + disks[i][2]:
                heights[i] = heights[j] + disks[i][2]
                prev[i] = j

        if maxHeight < heights[i]:
            maxHeight = heights[i]
            maxIdx = i

    return createList(disks, prev, maxIdx)


def createList(disks, prev, maxIdx):
    res = []
    idx = maxIdx
    while idx is not None:
        res.append(disks[idx])
        idx = prev[idx]

    return list(reversed(res))


def less(xs, ys):
    if xs[0] < ys[0] and xs[1] < ys[1] and xs[2] < ys[2]:
        return True
    return False


if __name__ == '__main__':
    # input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
    input = [[2, 1, 2],[3, 2, 3],[2, 2, 8],[2, 3, 4],[1, 3, 1],[4, 4, 5]]
    expected = [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
    actual = diskStacking(input)
    print(actual)
    assert(actual == expected)

