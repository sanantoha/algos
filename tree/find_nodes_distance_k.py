
from collections import deque


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    if tree is None or k < 0:
        return []

    parents = {}
    populateNodesToParents(tree, None, parents)

    targetNode = getNodeFromValue(target, tree, parents)

    queue = deque()
    queue.append((targetNode, 0))
    seen = set()
    seen.add(targetNode.value)

    while queue:
        node, distance = queue.popleft()

        if distance == k:
            res = [node.value for node, _ in queue]
            res.append(node.value)
            return res

        connectNodes = [node.left, node.right, parents[node.value]]

        for connectNode in connectNodes:
            if not connectNode:
                continue
            if connectNode.value in seen:
                continue

            seen.add(connectNode.value)
            queue.append((connectNode, distance + 1))

    return []


def getNodeFromValue(target, tree, parents):
    if tree.value == target:
        return tree

    parent = parents[target]

    if parent.left and parent.left.value == target:
        return parent.left
    else:
        return parent.right


def populateNodesToParents(node, parent, parents):
    if node:
        parents[node.value] = parent
        populateNodesToParents(node.left, node, parents)
        populateNodesToParents(node.right, node, parents)


# O(n) time | O(n) space
def findNodesDistanceK1(tree, target, k):
    if tree is None or k < 0:
        return []

    parents = {}
    seen = set()
    populateNodesToParents(tree, None, parents)

    targetNode = getNodeFromValue(target, tree, parents)

    res = []
    findNodesDistanceKRec(targetNode, 0, k, parents, seen, res)
    return res


def findNodesDistanceKRec(node, distance, k, parents, seen, res):
    if node is None or node.value in seen:
        return

    seen.add(node.value)

    if distance == k:
        res.append(node.value)
    else:
        findNodesDistanceKRec(node.left, distance + 1, k, parents, seen, res)
        findNodesDistanceKRec(node.right, distance + 1, k, parents, seen, res)
        findNodesDistanceKRec(parents[node.value], distance + 1, k, parents, seen, res)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.right.right.left = BinaryTree(7)
    root.right.right.right = BinaryTree(8)
    target = 3
    k = 2
    expected = [2, 7, 8]
    actual = findNodesDistanceK(root, target, k)
    print(actual)
    actual.sort()
    assert actual == expected

    actual = findNodesDistanceK1(root, target, k)
    print(actual)
    actual.sort()
    assert actual == expected