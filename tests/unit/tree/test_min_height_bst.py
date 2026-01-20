from tree.bst_traversal import in_order_traverse
from tree.min_height_bst import min_height_bst, get_tree_height
from tree.validate_bst import validate_bst


def test_min_height_bst():
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    tree = min_height_bst(array)

    assert validate_bst(tree)
    assert get_tree_height(tree) == 4

    in_order = in_order_traverse(tree, [])

    assert in_order == [1, 2, 5, 7, 10, 13, 14, 15, 22]