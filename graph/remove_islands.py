
# O(w * h) time | O(1) space
def remove_islands(matrix):
    if matrix is None or len(matrix) == 0:
        return matrix

    for row in range(len(matrix)):
        if matrix[row][0] == 1:
            dfs(matrix, row, 0)
        if matrix[row][-1] == 1:
            dfs(matrix, row, len(matrix[row]) - 1)

    for col in range(len(matrix[0])):
        if matrix[0][col] == 1:
            dfs(matrix, 0, col)
        if matrix[-1][col] == 1:
            dfs(matrix, len(matrix) - 1, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '*':
                matrix[row][col] = 1
            elif matrix[row][col] == 1:
                matrix[row][col] = 0

    return matrix


def dfs(matrix, row, col):
    if matrix[row][col] != 1:
        return

    matrix[row][col] = '*'
    neighbors = get_neighbors(matrix, row, col)
    for (next_row, next_col) in neighbors:
        if matrix[next_row][next_col] == 1:
            dfs(matrix, next_row, next_col)


def get_neighbors(matrix, row, col):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if row + 1 < len(matrix):
        neighbors.append((row + 1, col))
    if col + 1 < len(matrix[row]):
        neighbors.append((row, col + 1))

    return neighbors


if __name__ == '__main__':
    input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    expected = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    actual = remove_islands(input)
    print(actual)
    assert actual == expected