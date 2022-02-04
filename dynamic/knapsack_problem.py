
# O(n * c) time | O(n * c) space
def knapsackProblem(items, capacity):
    if items is None or len(items) == 0 or capacity <= 0:
        return [0, []]

    knapsackValues = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for idx in range(1, len(items) + 1):
        for cap in range(1, capacity + 1):
            (val, weight) = items[idx - 1]
            if weight > cap:
                knapsackValues[idx][cap] = knapsackValues[idx - 1][cap]
            else:
                knapsackValues[idx][cap] = max(knapsackValues[idx - 1][cap], knapsackValues[idx - 1][cap - weight] + val)

    # print(knapsackValues)

    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    res = []
    idx = len(knapsackValues) - 1
    cap = len(knapsackValues[0]) - 1

    while idx > 0:
        if knapsackValues[idx][cap] == knapsackValues[idx - 1][cap]:
            idx -= 1
        else:
            res.append(idx - 1)
            cap -= items[idx - 1][1]
            idx -= 1
        if cap == 0:
            break

    return list(reversed(res))


if __name__ == '__main__':
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    expected = [10, [1, 3]]
    actual = knapsackProblem(items, capacity)
    print(actual)
    assert actual == expected
