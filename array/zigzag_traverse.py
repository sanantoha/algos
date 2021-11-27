
# O(w * h) time | O(w * h) space
def zigzagTraverse(array):
    if array is None or len(array) == 0:
        return []

    res = []

    row = 0
    col = 0
    height = len(array) - 1
    width = len(array[0]) - 1

    isGoingDown = True

    while not isOutOfBound(row, col, height, width):
        res.append(array[row][col])
        if isGoingDown:
            if col == 0 or row == height:
                isGoingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1

            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                isGoingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1

            else:
                col += 1
                row -= 1

    return res


def isOutOfBound(row, col, height, width):
    return row < 0 or col < 0 or row > height or col > width


if __name__ == '__main__':
    test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
    actual = zigzagTraverse(test)
    print(actual)
    assert actual == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]