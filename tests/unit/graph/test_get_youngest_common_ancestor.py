from graph.get_youngest_common_ancestor import new_trees, get_youngest_common_ancestor


def test_get_youngest_common_ancestor():
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = get_youngest_common_ancestor(trees["A"], trees["E"], trees["I"])
    assert yca == trees["B"]