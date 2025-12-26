from collections import deque


# O(E + V) time | O(V) space
def can_finish(num_courses, prerequisites):
    if num_courses <= 0 or not prerequisites:
        return True

    adj_list = create_adj_list(num_courses, prerequisites)
    visited = [0] * num_courses

    for v in range(num_courses):
        if visited[v] == 0:
            if not dfs(adj_list, visited, v):
                return False

    return True


def dfs(adj_list, visited, v):
    visited[v] = 1

    for u in adj_list[v]:
        if visited[u] == 1:
            return False
        if visited[u] == 0:
            if not dfs(adj_list, visited, u):
                return False

    visited[v] = 2
    return True


def create_adj_list(num_courses, prerequisites):
    adj_list = [[] for _ in range(num_courses)]

    for [c, d] in prerequisites:
        adj_list[c].append(d)

    return adj_list


# O(E + V) time | O(V) space
def can_finish_kahn_algorithm(num_courses, prerequisites):
    if num_courses <= 0 or not prerequisites:
        return True

    adj_list = create_adj_list(num_courses, prerequisites)
    cnt = [0] * num_courses

    for v in range(num_courses):
        for u in adj_list[v]:
            cnt[u] += 1

    is_circle = True
    queue = deque()

    for v in range(len(cnt)):
        if cnt[v] == 0:
            queue.append(v)
            is_circle = False

    if is_circle:
        return False

    idx = 0

    while queue:
        v = queue.popleft()

        idx += 1

        for u in adj_list[v]:
            cnt[u] -= 1

            if cnt[u] == 0:
                queue.append(u)


    if num_courses != idx:
        return False

    return True


if __name__ == '__main__':
    assert can_finish(1, [])

    assert can_finish(2, [[1, 0]])

    assert not can_finish(2, [[1, 0], [0, 1]])

    assert not can_finish(4, [[1, 0], [2, 1], [3, 2], [0, 3]])

    assert can_finish(4, [[1, 0], [2, 1], [3, 2]])



    assert can_finish_kahn_algorithm(1, [])

    assert can_finish_kahn_algorithm(2, [[1, 0]])

    assert not can_finish_kahn_algorithm(2, [[1, 0], [0, 1]])

    assert not can_finish_kahn_algorithm(4, [[1, 0], [2, 1], [3, 2], [0, 3]])

    assert can_finish_kahn_algorithm(4, [[1, 0], [2, 1], [3, 2]])