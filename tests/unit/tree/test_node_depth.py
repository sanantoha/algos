import pytest

from tree.BinaryTree import BinaryTree
from tree.node_depths import node_depths, node_depths1, node_depths2


def create_root():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    return root


TEST_CASE = [
    (create_root(), 16)
]


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_node_depth(root, exp):
    assert node_depths(root) == exp


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_node_depth1(root, exp):
    assert node_depths1(root) == exp


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_node_depth2(root, exp):
    assert node_depths2(root) == exp