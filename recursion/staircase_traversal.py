
# O(maxSteps ^ height) time | O(maxSteps ^ height) space
def staircaseTraversal(height, maxSteps):
    if height == 0:
        return 1

    cnt = 0
    for i in range(1, min(height + 1, maxSteps + 1)):
        cnt += staircaseTraversal(height - i, maxSteps)
    return cnt


# O(height * maxSteps) time | O(height) space
def staircaseTraversalMemo(height, maxSteps):
    return staircaseTraversalMemoRec(height, maxSteps, {0: 1, 1: 1})


def staircaseTraversalMemoRec(height, maxSteps, memoiz):
    if height in memoiz:
        return memoiz[height]

    cnt = 0
    for i in range(1, min(height + 1, maxSteps + 1)):
        cnt += staircaseTraversalMemoRec(height - i, maxSteps, memoiz)

    memoiz[height] = cnt
    return cnt


# O(height * maxSteps) time | O(height) space
def staircaseTraversalIter(height, maxSteps):
    if height == 0:
        return 1

    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1

    for i in range(1, height + 1):
        step = 1
        while step <= maxSteps and step <= i:
            waysToTop[i] += waysToTop[i - step]
            step += 1

    return waysToTop[height]


# O(height) time | O(height) space
def staircaseTraversalWindow(height, maxSteps):
    if height == 0:
        return 1

    waysToTop = [1]

    currWays = 0
    for i in range(1, height + 1):
        startWindow = i - maxSteps - 1
        if startWindow >= 0:
            currWays -= waysToTop[startWindow]

        endWindow = i - 1
        currWays += waysToTop[endWindow]
        waysToTop.append(currWays)

    return currWays


if __name__ == '__main__':
    stairs = 4
    maxSteps = 2
    expected = 5
    actual = staircaseTraversal(stairs, maxSteps)
    print(actual)
    assert actual == expected

    actual = staircaseTraversalMemo(stairs, maxSteps)
    print(actual)
    assert actual == expected

    actual = staircaseTraversalIter(stairs, maxSteps)
    print(actual)
    assert actual == expected

    actual = staircaseTraversalWindow(stairs, maxSteps)
    print(actual)
    assert actual == expected