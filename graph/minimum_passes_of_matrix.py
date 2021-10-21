
from collections import deque


# O(w * h) time | O(w * h) space
def minimum_passes_of_matrix(matrix):
    if matrix is None or len(matrix) == 0:
        return -1

    res = 0
    queue = get_all_positive_positions(matrix)

    while queue:
        size = len(queue)

        while size > 0:
            row, col = queue.popleft()
            neighbors = get_neighbors(matrix, row, col)
            for n_row, n_col in neighbors:
                if matrix[n_row][n_col] < 0:
                    matrix[n_row][n_col] *= -1
                    queue.append((n_row, n_col))
            size -= 1

        res += 1

    return -1 if contains_negative(matrix) else res - 1


def get_all_positive_positions(matrix):
    queue = deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                queue.append((row, col))

    return queue


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


def contains_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


if __name__ == '__main__':
    input = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    expected = 3
    actual = minimum_passes_of_matrix(input)
    print(actual)
    assert actual == expected