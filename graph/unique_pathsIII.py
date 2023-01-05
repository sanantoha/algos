
# https://leetcode.com/problems/unique-paths-iii/description/
# You are given an m x n integer array grid where grid[i][j] could be:
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.


# O(3 ^ n) time | O(n) space - where n length of cells
def uniquePathsIII(grid):
    startRow = 0
    startCol = 0

    zeros = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                zeros += 1
            elif grid[i][j] == 1:
                startRow = i
                startCol = i

    return path(grid, startRow, startCol, zeros)

def path(grid, row, col, zeros):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == -1:
        return 0

    if grid[row][col] == 2:
        return 1 if zeros == -1 else 0

    grid[row][col] = -1
    zeros -= 1

    totalCount = path(grid, row - 1, col, zeros) + \
                 path(grid, row, col - 1, zeros) + \
                 path(grid, row + 1, col, zeros) + \
                 path(grid, row, col + 1, zeros)

    zeros += 1
    grid[row][col] = 1

    return totalCount


if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    actual = uniquePathsIII(grid)
    print(actual)
    assert actual == 2


