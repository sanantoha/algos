
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(1) space
def find_successor(tree, node):
    if tree is None or node is None:
        return None

    if node.right is not None:
        return get_most_left(node.right)

    return get_most_parent(node)


def get_most_parent(node):
    curr = node
    while curr.parent and curr.parent.right == curr:
        curr = curr.parent

    return curr.parent


def get_most_left(node):
    curr = node
    while curr.left:
        curr = curr.left

    return curr


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    expected = root
    actual = find_successor(root, node)
    assert actual == expected