from tree.BinaryTree import BinaryTree
from tree.evaluate_expression_tree import evaluateExpressionTree


def test_evaluateExpressionTree():
    tree = BinaryTree(-1)
    tree.left = BinaryTree(-2)
    tree.left.left = BinaryTree(-4)
    tree.left.right = BinaryTree(2)
    tree.left.left.left = BinaryTree(3)
    tree.left.left.right = BinaryTree(2)

    tree.right = BinaryTree(-3)
    tree.right.left = BinaryTree(8)
    tree.right.right = BinaryTree(3)
    expected = 6
    actual = evaluateExpressionTree(tree)
    print(actual)
    assert actual == expected