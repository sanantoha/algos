
from BinaryTree import BinaryTree


def get_tree_info(tree):
    if tree is None:
        return TreeInfo(0, 0)

    li = get_tree_info(tree.left)
    ri = get_tree_info(tree.right)

    longest_path = li.height + ri.height
    max_diameter = max(li.diameter, ri.diameter)
    diameter = max(longest_path, max_diameter)
    height = 1 + max(li.height, ri.height)

    return TreeInfo(height, diameter)

# O(n) time | O(h) space
def binary_tree_diameter(tree):
    return get_tree_info(tree).diameter


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


if __name__ == '__main__':
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