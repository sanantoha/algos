
# O(w * h) time | O(w * h) space
def transposeMatrix(matrix):
    res = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)

    return res


if __name__ == '__main__':
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    actual = transposeMatrix(input)
    print(actual)

    assert actual == expected