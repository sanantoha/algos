
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadth_first_search(self, array):

        queue = deque()
        queue.append(self)

        while queue:
            curr = queue.popleft()
            array.append(curr.name)

            for child in curr.children:
                queue.append(child)

        return array


if __name__ == '__main__':
    graph = Node("A")
    graph.add_child("B").add_child("C").add_child("D")
    graph.children[0].add_child("E").add_child("F")
    graph.children[2].add_child("G").add_child("H")
    graph.children[0].children[1].add_child("I").add_child("J")
    graph.children[2].children[0].add_child("K")

    print(graph.breadth_first_search([]))
    assert graph.breadth_first_search([]) == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]