
from tree.validate_bst import validate_bst
from tree.bst_traversal import in_order_traverse
from tree.BST import BST


# O(n) time | O(n) space
def min_height_bst(array):
    return min_height_bst_helper(array, 0, len(array) - 1)


def min_height_bst_helper(array, l, r):
    if l > r:
        return None
    mid = (l + r) // 2
    root = BST(array[mid])
    root.left = min_height_bst_helper(array, l, mid - 1)
    root.right = min_height_bst_helper(array, mid + 1, r)
    return root


def get_tree_height(tree, height=0):
    if tree is None:
        return height
    left_tree_height = get_tree_height(tree.left, height + 1)
    right_tree_height = get_tree_height(tree.right, height + 1)
    return max(left_tree_height, right_tree_height)


if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    tree = min_height_bst(array)

    assert validate_bst(tree)
    assert get_tree_height(tree) == 4

    in_order = in_order_traverse(tree, [])

    assert in_order == [1, 2, 5, 7, 10, 13, 14, 15, 22]