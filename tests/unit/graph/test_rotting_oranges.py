from graph.rotting_oranges import oranges_rotting


def test_rotting_oranges_case1():
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


def test_rotting_oranges_case2():
    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == -1


def test_rotting_oranges_case3():
    grid = [
        [0,2]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == 0


def test_rotting_oranges_case4():
    grid = [
        [0]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == 0


def test_rotting_oranges_case5():
    grid = [
        [1]
    ]
    res = oranges_rotting(grid)
    print(res)
    assert res == -1