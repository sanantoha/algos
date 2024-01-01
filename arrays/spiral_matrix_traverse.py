
# O(w * h) time | O(1) space
def spiral_matrix_traverse(matrix):
    res = []
    if matrix is None or len(matrix) == 0:
        return res

    start_row, start_col = 0, 0
    end_row = len(matrix) - 1
    end_col = len(matrix[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            res.append(matrix[start_row][i])
        start_row += 1

        for i in range(start_row, end_row + 1):
            res.append(matrix[i][end_col])
        end_col -= 1

        if start_row <= end_row and start_col <= end_col:
            for i in reversed(range(start_col, end_col + 1)):
                res.append(matrix[end_row][i])
            end_row -= 1

            for i in reversed(range(start_row, end_row + 1)):
                res.append(matrix[i][start_col])
            start_col += 1

    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]]
    print(spiral_matrix_traverse(matrix))
