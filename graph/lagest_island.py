
# O(w ^ 2 * h ^ 2) time | O(w * h) space
def largestIsland(matrix):
    if not matrix:
        return -1

    maxSize = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                continue

            maxSize = max(maxSize, dfs(matrix, row, col))

    return maxSize


def dfs(matrix, row, col):
    size = 1
    visited = [[False for _ in row] for row in matrix]
    visited[row][col] = True

    neighbors = getNeighbors(matrix, row, col)

    while neighbors:
        (currRow, currCol) = neighbors.pop()

        if visited[currRow][currCol] or matrix[currRow][currCol] != 0:
            continue

        visited[currRow][currCol] = True
        size += 1

        for (nrow, ncol) in getNeighbors(matrix, currRow, currCol):
            neighbors.append((nrow, ncol))

    return size


def getNeighbors(matrix, row, col):
    n = []

    if row > 0:
        n.append((row - 1, col))
    if col > 0:
        n.append((row, col - 1))
    if row + 1 < len(matrix):
        n.append((row + 1, col))
    if col + 1 < len(matrix[row]):
        n.append((row, col + 1))

    return n


# O(w * h) time | O(w * h) space
def largestIsland1(matrix):
    if not matrix:
        return -1

    islandSizes = []

    islandNumber = 2

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                continue

            islandSizes.append(dfsIslandSize(matrix, row, col, islandNumber))
            islandNumber += 1

    maxSize = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                continue

            islands = set()
            for (nrow, ncol) in getNeighbors(matrix, row, col):
                if matrix[nrow][ncol] != 1:
                    islands.add(matrix[nrow][ncol])

            size = 1
            for island in islands:
                size += islandSizes[island - 2]

            maxSize = max(maxSize, size)

    return maxSize



def dfsIslandSize(matrix, startRow, startCol, islandNumber):
    size = 0
    stack = [(startRow, startCol)]

    while stack:
        (row, col) = stack.pop()

        if matrix[row][col] != 0:
            continue

        matrix[row][col] = islandNumber
        size += 1

        stack += getNeighbors(matrix, row, col)

    return size


if __name__ == '__main__':
    matrix = [
        [1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0]
    ]
    expected = 8

    actual = largestIsland(matrix)
    print(actual)
    assert actual == expected

    actual = largestIsland1(matrix)
    print(actual)
    assert actual == expected