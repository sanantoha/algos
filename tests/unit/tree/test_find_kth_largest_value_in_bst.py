from tree.BST import BST
from tree.find_kth_largest_value_in_bst import find_kth_largest_value_in_bst


def test_find_kth_largest_value_in_bst():
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3
    expected = 17
    actual = find_kth_largest_value_in_bst(root, k)
    print(actual)
    assert actual == expected