
# https://www.algoexpert.io/questions/Water%20Area
# O(n) time | O(n) space
def waterArea(heights):

    leftMax = [0] * len(heights)
    rightMax = [0] * len(heights)

    for i in range(1, len(heights)):
        leftMax[i] = max(heights[i - 1], leftMax[i - 1])

    for i in reversed(range(len(heights) - 1)):
        rightMax[i] = max(heights[i + 1], rightMax[i + 1])

    maxWaterArea = 0

    for i in range(len(heights)):
        minHeight = min(leftMax[i], rightMax[i])
        if minHeight > 0 and heights[i] < minHeight:
            maxWaterArea += minHeight - heights[i]

    return maxWaterArea


# O(n) time | O(n) space
def waterArea1(heights):
    maxes = [0 for _ in heights]
    leftMax = 0

    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)

    rightMax = 0

    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(maxes[i], rightMax)
        maxes[i] = minHeight - height if minHeight > height else 0
        rightMax = max(rightMax, height)

    return sum(maxes)


# O(n) time | O(1) space
def waterArea2(heights):
    if len(heights) == 0:
        return 0

    l = 0
    r = len(heights) - 1
    leftMax = heights[l]
    rightMax = heights[r]
    surfaceArea = 0

    while l < r:
        if heights[l] < heights[r]:
            l += 1
            leftMax = max(leftMax, heights[l])
            surfaceArea += leftMax - heights[l]
        else:
            r -= 1
            rightMax = max(rightMax, heights[r])
            surfaceArea += rightMax - heights[r]

    return surfaceArea


if __name__ == '__main__':
    expected = 48
    actual = waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
    print(actual)
    print(actual == expected)

    actual = waterArea1([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
    print(actual)
    print(actual == expected)

    actual = waterArea2([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
    print(actual)
    print(actual == expected)