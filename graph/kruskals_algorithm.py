# O(E * log(E)) time | O(E + V) space
def kruskalsAlgorithm(graph):
    if not graph:
        return []

    edges = []
    for v in range(len(graph)):
        for u, w in graph[v]:
            if v < u:
                edges.append([v, u, w])

    edges.sort(key=lambda edge: edge[2]) # O(E * log(E)) time

    parents = [i for i in range(len(graph))] # O(V) space
    rank = [0 for _ in range(len(graph))] # O(V) space

    newGraph = [[] for _ in range(len(graph))] # O(E + V) space

    for v, u, w in edges:
        pv = find(parents, v)
        pu = find(parents, u)

        if pv != pu:
            newGraph[v].append([u, w])
            newGraph[u].append([v, w])
            union(parents, rank, v, u)

    return newGraph


def find(parents, v):
    if parents[v] == v:
        return v
    parents[v] = find(parents, parents[v])
    return parents[v]


def union(parents, rank, pv, pu):
    if rank[pv] < rank[pu]:
        parents[pv] = pu
    elif rank[pv] > rank[pu]:
        parents[pu] = pv
    else:
        parents[pu] = pv
        rank[pv] += 1


if __name__ == '__main__':
    input = [
        [[1, 3],[2, 5]],
        [[0, 3],[2, 10],[3, 12]],
        [[0, 5],[1, 10]],
        [[1, 12]]
    ]

    expected = [
        [[1, 3],[2, 5]],
        [[0, 3],[3, 12]],
        [[0, 5]],
        [[1, 12]]
    ]
    actual = kruskalsAlgorithm(input)
    print(actual, "     =    ", expected)
    assert actual == expected