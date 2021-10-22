
# O(n * log(n)) time | O(n)
def task_assignment(k, tasks):
    map = {}
    for i, task in enumerate(tasks):
        lst = map.get(task, [])
        lst.append(i)
        map[task] = lst

    tasks.sort()

    l = 0
    r = len(tasks) - 1

    res = []
    while l < r:
        lv = map[tasks[l]].pop()
        rv = map[tasks[r]].pop()
        res.append([lv, rv])
        l += 1
        r -= 1

    return res


if __name__ == '__main__':
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    expected = [[4, 2], [0, 5], [3, 1]]
    actual = task_assignment(k, tasks)
    print(actual)
    assert actual == expected