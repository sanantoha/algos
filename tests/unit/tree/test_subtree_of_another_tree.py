from tree.BinaryTree import BinaryTree
from tree.subtree_of_another_tree import is_subtree


def test_subtree_of_another_tree():
    root1 = BinaryTree(3)
    root1.left = BinaryTree(4)
    root1.left.left = BinaryTree(1)
    root1.left.right = BinaryTree(2)
    root1.right = BinaryTree(5)

    sub_tree = BinaryTree(4)
    sub_tree.left = BinaryTree(1)
    sub_tree.right = BinaryTree(2)

    res = is_subtree(root1, sub_tree)
    print(res)  # True
    assert res

    root2 = BinaryTree(3)
    root2.left = BinaryTree(4)
    root2.left.left = BinaryTree(1)
    root2.left.right = BinaryTree(2)
    root2.left.right.left = BinaryTree(0)
    root2.right = BinaryTree(5)

    res = is_subtree(root2, sub_tree)
    print(res)  # False
    assert not res

    root3 = BinaryTree(4)
    root3.left = BinaryTree(4)
    root3.left.left = BinaryTree(4)
    root3.left.left.left = BinaryTree(4)
    root3.left.left.left.left = BinaryTree(4)
    root3.left.left.left.left.left = BinaryTree(1)
    root3.left.left.left.left.right = BinaryTree(2)

    res = is_subtree(root3, sub_tree)
    print(res) # True
    assert res
