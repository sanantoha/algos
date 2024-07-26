
# O(w * h) time | O(w * h) space
def numberOfIsland(matrix):
    if not matrix:
        return -1

    totalNumber = 0

    visited = [[False for _ in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col] and matrix[row][col] == 1:
                totalNumber += 1
                dfs(matrix, visited, row, col)

    return totalNumber


def dfs(matrix, visited, startRow, startCol):
    stack = [(startRow, startCol)]

    while stack:
        (row, col) = stack.pop()

        if visited[row][col]:
            continue

        visited[row][col] = True

        for (nrow, ncol) in getNeighbors(matrix, row, col):
            if matrix[nrow][ncol] != 1:
                continue

            stack.append((nrow, ncol))


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


if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    expected = 3

    actual = numberOfIsland(matrix)
    print(actual)
    assert actual == expected