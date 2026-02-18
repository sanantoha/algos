from tree.BinaryTree import BinaryTree
from tree.binary_tree_diameter import binary_tree_diameter


def test_binary_tree_diameter():
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.left.left = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.right = BinaryTree(2)
    expected = 6
    actual = binary_tree_diameter(root)
    print(actual)
    assert actual == expected