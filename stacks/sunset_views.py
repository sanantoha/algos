
# O(n) time | O(n) time
def sunsetViews(buildings, direction):
    if buildings is None or len(buildings) == 0:
        return []
    if direction == 'EAST':
        return getEastBuildings(buildings)
    else:
        return getWestBuildings(buildings)


def getEastBuildings(buildings):
    stack = []
    maxBuilding = len(buildings) - 1
    stack.append(maxBuilding)

    for i in reversed(range(0, len(buildings) - 1)):
        if buildings[i] > buildings[maxBuilding]:
            stack.append(i)
            maxBuilding = i

    res = []
    while stack:
        res.append(stack.pop())

    return res


def getWestBuildings(buildings):
    res = []
    maxBuilding = 0
    res.append(maxBuilding)
    for i in range(1, len(buildings)):
        if buildings[maxBuilding] < buildings[i]:
            res.append(i)
            maxBuilding = i

    return res


if __name__ == '__main__':
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST"
    expected = [1, 3, 6, 7]
    actual = sunsetViews(buildings, direction)
    print(actual)
    assert actual == expected

    direction = "WEST"
    expected = [0, 1]
    actual = sunsetViews(buildings, direction)
    print(actual)
    assert actual == expected