from graph.breadth_first_search import Node


def test_breadth_first_search():
    graph = Node("A")
    graph.add_child("B").add_child("C").add_child("D")
    graph.children[0].add_child("E").add_child("F")
    graph.children[2].add_child("G").add_child("H")
    graph.children[0].children[1].add_child("I").add_child("J")
    graph.children[2].children[0].add_child("K")

    print(graph.breadth_first_search([]))
    assert graph.breadth_first_search([]) == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]