
# O(V + E) time | O(V) space
def twoColorable(edges):
    if not edges:
        return True

    colors = [None] * len(edges)
    colors[0] = True

    stack = [0]

    while stack:
        v = stack.pop()

        for u in edges[v]:
            if not colors[u]:
                colors[u] = not colors[v]
                stack.append(u)
            elif colors[u] == colors[v]:
                return False

    return True


if __name__ == '__main__':
    input = [
        [1, 2, 3],
        [0, 2],
        [0, 1],
        [0]
    ]
    actual = twoColorable(input)
    print(actual)
    assert not actual

    input = [
        [2],
        [2, 3],
        [0, 1],
        [1]
    ]

    actual = twoColorable(input)
    print(actual)
    assert actual