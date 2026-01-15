import pytest


from tree.BST import BST
from tree.find_closest_value_in_bst import find_closest_value_in_bst, find_closest_value_in_bst1, \
    find_closest_value_in_bst2


def create_root():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    return root


TEST_CASE = [
    (create_root(), 13)
]


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_find_closest_value_in_bst(root, exp):
    assert find_closest_value_in_bst(root, 12) == exp


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_find_closest_value_in_bst1(root, exp):
    assert find_closest_value_in_bst1(root, 12) == exp


@pytest.mark.parametrize("root, exp", TEST_CASE)
def test_find_closest_value_in_bst2(root, exp):
    assert find_closest_value_in_bst2(root, 12) == exp