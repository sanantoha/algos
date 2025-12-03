from graph.cycle_in_graph import cycle_in_graph, cycle_in_graph1


input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
expected = True


def test_cycle_in_the_graph():
    actual = cycle_in_graph(input)
    print(actual)
    assert actual == expected


def test_cycle_in_the_graph1():
    actual = cycle_in_graph1(input)
    print(actual)
    assert actual == expected