
from collections import deque

def oranges_rotting(grid):
    if not grid:
        return 0

    queue = find_all_rotten(grid)
    if len(queue) == 0:
        if is_all_rotten(grid):
            return 0
        else:
            return -1

    count = 0

    while queue:
        size = len(queue)

        count += 1

        while size > 0:
            size -= 1

            (row, col) = queue.popleft()
            for n_row, n_col in get_neghborns(grid, row, col):
                if grid[n_row][n_col] == 1:
                    grid[n_row][n_col] = 2
                    queue.append((n_row, n_col))



    if is_all_rotten(grid):
        return count - 1
    else:
        return -1


def find_all_rotten(grid):
    queue = deque()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 2:
                queue.append((row, col))

    return queue

def is_all_rotten(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                return False

    return True


def get_neghborns(grid, row, col):
    n = []
    if row > 0:
        n.append((row - 1, col))
    if col > 0:
        n.append((row, col - 1))
    if row + 1 < len(grid):
        n.append((row + 1, col))
    if col + 1 < len(grid[row]):
        n.append((row, col + 1))
    return n


if __name__ == '__main__':
    # 0 - no orange, empty cell
    # 1 - orange is fresh
    # 2 - orange is rotten
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == 4

    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == -1

    grid = [
        [0,2]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == 0

    grid = [
        [0]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == 0

    grid = [
        [1]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == -1
