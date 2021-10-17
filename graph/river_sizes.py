

# O(w * h) time | O(w * h) space
def river_sizes(matrix):
    res = []
    if matrix is None or len(matrix) == 0:
        return res

    visited = [[False for _ in range(len(matrix[row]))] for row in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col] and matrix[row][col] == 1:
                res.append(dfs(matrix, visited, row, col, 0))

    return res


def dfs(matrix, visited, row, col, count):
    visited[row][col] = True
    count += 1
    next_steps = get_next_steps(matrix, row, col)

    for (next_row, next_col) in next_steps:
        if not visited[next_row][next_col] and matrix[next_row][next_col] == 1:
            count = dfs(matrix, visited, next_row, next_col, count)

    return count


def get_next_steps(matrix, row, col):
    res = []

    if row > 0:
        res.append((row - 1, col))

    if col > 0:
        res.append((row, col - 1))

    if (row + 1) < len(matrix):
        res.append((row + 1, col))

    if (col + 1) < len(matrix[row]):
        res.append((row, col + 1))

    return res


if __name__ == '__main__':
    # test_input = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
    test_input = [
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 1., 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    ]

    expected = [1, 1, 2, 2, 5, 21]
    # expected = [1, 2, 2, 2, 5]

    actual = sorted(river_sizes(test_input))
    print(actual)
    assert actual == expected
