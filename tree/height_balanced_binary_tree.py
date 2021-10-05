
from BinaryTree import BinaryTree


# O(n) time | O(h) space
def height_balanced_binary_tree(tree):
    if tree is None:
        return True

    if tree.left is None and tree.right is None:
        return True
    elif tree.left is None:
        if tree.right.right is not None or tree.right.left is not None:
            return False
        return True
    elif tree.right is None:
        if tree.left.left is not None or tree.left.right is not None:
            return False
        return True
    else:
        return height_balanced_binary_tree(tree.left) and height_balanced_binary_tree(tree.right)


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def height_balanced_binary_tree1(tree):
    return get_tree_info(tree).is_balanced


def get_tree_info(tree):
    if tree is None:
        return TreeInfo(True, -1)

    left_info = get_tree_info(tree.left)
    right_info = get_tree_info(tree.right)

    is_balanced = left_info.is_balanced and right_info.is_balanced \
                  and abs(left_info.height - right_info.height) <= 1

    height = max(left_info.height, right_info.height) + 1
    return TreeInfo(is_balanced, height)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)
    expected = True
    actual = height_balanced_binary_tree(root)
    assert actual == expected

    actual1 = height_balanced_binary_tree1(root)
    assert actual1 == expected