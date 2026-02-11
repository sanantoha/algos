from graph.depth_first_search import Node


def test_depth_first_search():
    graph = Node("A")
    graph.add_child("B").add_child("C").add_child("D")
    graph.children[0].add_child("E").add_child("F")
    graph.children[2].add_child("G").add_child("H")
    graph.children[0].children[1].add_child("I").add_child("J")
    graph.children[2].children[0].add_child("K")
    assert graph.depth_first_search([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]