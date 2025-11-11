import collections


# O(w * h) time | O(w * h) space
def update_matrix(matrix):
    if not matrix:
        return matrix

    replace_one_on_max_val(matrix)

    queue = find_all_zeros(matrix)

    while queue:
        (row, col, level) = queue.popleft()

        for (nrow, ncol) in get_neighborns(matrix, row, col):
            if matrix[nrow][ncol] == float('inf'):
                matrix[nrow][ncol] = level + 1
                queue.append((nrow, ncol, matrix[nrow][ncol]))


    return matrix


def get_neighborns(matrix, row, col):
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


def find_all_zeros(matrix):
    queue = collections.deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                queue.append((row, col, 0))

    return queue


def replace_one_on_max_val(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = float('inf')


if __name__ == '__main__':
    input0 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    res = update_matrix(input0)
    print(res)
    assert res == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    input1 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]

    res = update_matrix(input1)
    print(res)
    assert res == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]