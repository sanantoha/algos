from tree.BinaryTree import BinaryTree
from collections import deque


# O(n) time | O(n) space
def node_depths(root):
    sum_of_depths = 0
    queue = deque()

    queue.append(root)

    level = 0
    while queue:
        size = len(queue)

        while size > 0:
            node = queue.popleft()
            size -= 1
            sum_of_depths += level
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        level += 1

    return sum_of_depths


# O(n) time | O(h) space
def node_depths1(root, depth=0):
    if root is None:
        return 0
    return depth + node_depths1(root.left, depth + 1) + node_depths1(root.right, depth + 1)


# O(n) time | O(h) space
def node_depths2(root):
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]

    while stack:
        node_item = stack.pop()
        node, depth = node_item["node"], node_item["depth"]
        if node is None:
            continue

        sum_of_depths += depth

        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sum_of_depths


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(node_depths(root) == 16)
    print(node_depths1(root) == 16)
    print(node_depths2(root) == 16)
