
# O(w * h) time | O(w * h) space
def remove_islands(matrix):
    if matrix is None or len(matrix) == 0:
        return matrix

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            row_is_border = row == 0 or row == len(matrix) - 1
            col_is_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_is_border or col_is_border

            if not is_border or matrix[row][col] != 1:
                continue

            dfs(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
            elif matrix[row][col] == 2:
                matrix[row][col] = 1

    return matrix


def dfs(matrix, row, col):
    stack = [(row, col)]

    while stack:
        (curr_row, curr_col) = stack.pop()

        matrix[curr_row][curr_col] = 2
        neighbors = get_neighbors(matrix, curr_row, curr_col)

        for (next_row, next_col) in neighbors:
            if matrix[next_row][next_col] != 1:
                continue

            stack.append((next_row, next_col))


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