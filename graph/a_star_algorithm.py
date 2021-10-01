
import heapq


# O(w * h * log(w * h)) time | O(w * h) space
def a_star_algorithm(start_row, start_col, end_row, end_col, graph):
    nodes = init_nodes(graph)
    start_node = nodes[start_row][start_col]
    end_node = nodes[end_row][end_col]
    start_node.distance_from_start = 0
    start_node.estimated_distance_to_end = calculate_manhattan_distance(start_node, end_node)

    heap = [start_node]

    while heap:
        min_node = heapq.heappop(heap)
        if min_node == end_node:
            break

        neighbors = get_neighbors(min_node, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue

            tentative_distance = min_node.distance_from_start + 1
            if tentative_distance >= neighbor.distance_from_start:
                continue

            neighbor.came_from = min_node
            neighbor.distance_from_start = tentative_distance
            neighbor.estimated_distance_to_end = tentative_distance + calculate_manhattan_distance(neighbor, end_node)

            if neighbor in heap:
                # there is no update method in heapq which has complexity O(log(n)) time
                # for simplicity use heapify which update heap but takes O(n) time
                heapq.heapify(heap)
            else:
                heapq.heappush(heap, neighbor)

    return recreate_path(end_node)


def recreate_path(end_node):
    path = []
    if end_node.came_from is None:
        return path

    curr = end_node
    while curr:
        path.append([curr.row, curr.col])
        curr = curr.came_from

    return path[::-1]


def get_neighbors(min_node, nodes):
    neighbors = []

    row = min_node.row
    col = min_node.col

    if row > 0:
        neighbors.append(nodes[row - 1][col])

    if col > 0:
        neighbors.append(nodes[row][col - 1])

    if row + 1 < len(nodes):
        neighbors.append(nodes[row + 1][col])

    if col + 1 < len(nodes[row]):
        neighbors.append(nodes[row][col + 1])

    return neighbors


def calculate_manhattan_distance(start_node, end_node):
    return abs(end_node.row - start_node.row) + abs(end_node.col - start_node.col)


def init_nodes(graph):
    res = []

    for i, arr in enumerate(graph):
        res.append([])
        for j, v in enumerate(arr):
            res[i].append(Node(i, j, v))

    return res


class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.distance_from_start = float('inf')
        self.estimated_distance_to_end = float('inf')
        self.came_from = None

    def __lt__(self, other):
        return self.estimated_distance_to_end < other.estimated_distance_to_end


if __name__ == '__main__':
    start_row = 0
    start_col = 1
    end_row = 4
    end_col = 3
    graph = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 0, 0, 0]]
    expected = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
    actual = a_star_algorithm(start_row, start_col, end_row, end_col, graph)
    print(actual)
    assert actual == expected
