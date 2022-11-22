
# O(2 ^ N) time | O(N) space
def allPathsSourceTarget0(self, graph):
    if not graph:
        return []

    start = 0
    res = []
    ans = [start]
    self.dfs(graph, start, ans, res)
    return res


def dfs(self, graph, v, ans, res):
    if v == len(graph) - 1:
        res.append(ans[:])
        return

    for u in graph[v]:
        ans.append(u)
        self.dfs(graph, u, ans, res)
        ans.pop()

# O(E + 2^(N-2)*V) time | O(N) space
def allPathsSourceTarget(graph):
    # edges cases:
    if not graph:
        return []

    # apply DFS on DAG
    n = len(graph)
    stack = [(0, [0])]  # - store noth the (node, and the path leading to it)
    res = []
    while stack:
        node, path = stack.pop()
        # check leaf
        if node == n - 1:
            res.append(path)
        # traverse rest
        for nei in graph[node]:
            stack.append((nei, path + [nei]))
    return res



# https://leetcode.com/problems/all-paths-from-source-to-target/
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).
if __name__ == '__main__':
    print(allPathsSourceTarget([[1, 2], [3], [3], []])) # [[0, 2, 3], [0, 1, 3]]
    print(allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []])) # [[0, 1, 4], [0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 3, 4], [0, 4]]
    print(allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [], [4], []])) # [[0, 1, 4], [0, 1, 3, 4], [0, 3, 4], [0, 4]]
    print(allPathsSourceTarget([[2], [], [1]])) # [[0, 2]]