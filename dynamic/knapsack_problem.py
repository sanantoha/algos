
def knapsackProblem(items, capacity):
    if items is None or len(items) == 0 or capacity <= 0:
        return [0, []]

    knapsackValues = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for idx in range(1, len(items) + 1):
        for cap in range(1, capacity + 1):
            (val, weight) = items[idx - 1]
            if cap >= weight:
                knapsackValues[idx][cap] = val + knapsackValues[idx - 1][cap - weight]

    print(knapsackValues)

    pass


if __name__ == '__main__':
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    expected = [10, [1, 3]]
    actual = knapsackProblem(items, capacity)
    print(actual)
    assert actual == expected
