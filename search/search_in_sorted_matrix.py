
# O(w + h) time | O(1) space
def searchInSortedMatrix(matrix, target):
    if matrix is None or len(matrix) == 0:
        return [-1, -1]

    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return [row, col]

    return [-1, -1]


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    actual = searchInSortedMatrix(matrix, 44)
    print(actual)
    assert actual == [3, 3]