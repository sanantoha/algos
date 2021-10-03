
from BinaryTree import BinaryTree
from collections import deque


# O(n) time | O(d) space
def invert_binary_tree(tree):
    if tree is None:
        return

    tree.left, tree.right = tree.right, tree.left

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)


# O(n) time | O(n) space
def invert_binary_tree_iter(tree):
    queue = deque()
    queue.append(tree)

    while queue:
        curr = queue.popleft()

        if curr is None:
            continue

        curr.left, curr.right = curr.right, curr.left

        queue.append(curr.left)
        queue.append(curr.right)


if __name__ == '__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
    inverted_tree = BinaryTree(1).inverted_insert([2, 3, 4, 5, 6, 7, 8, 9])
    invert_binary_tree(tree)
    assert tree.__eq__(inverted_tree)

    tree1 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
    inverted_tree1 = BinaryTree(1).inverted_insert([2, 3, 4, 5, 6, 7, 8, 9])
    invert_binary_tree_iter(tree1)
    assert tree1.__eq__(inverted_tree1)
