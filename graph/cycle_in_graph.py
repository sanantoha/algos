
# O(E + V) time | O(V) space
def cycle_in_graph(edges):

    visited = [0 for _ in range(len(edges))]

    for v in range(len(edges)):
        if visited[v] == 0:
            if dfs(edges, v, visited):
                return True

    return False


def dfs(edges, v, visited):
    visited[v] = 1

    for u in edges[v]:
        if visited[u] == 1:
            return True
        if visited[u] == 0:
            if dfs(edges, u, visited):
                return True

    visited[v] = 2
    return False


if __name__ == '__main__':
    input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    expected = True
    actual = cycle_in_graph(input)
    print(actual)
    assert actual == expected