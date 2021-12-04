
# O(n) time | O(log(n)) space
def maxPathSum(tree):
    _, maxPath = findMaxPath(tree)
    return maxPath


def findMaxPath(tree):
    if tree is None:
        return (0, float('-inf'))

    leftMaxPathAsBranch, leftMaxPath = findMaxPath(tree.left)
    rightMaxPathAsBranch, rightMaxPath = findMaxPath(tree.right)
    maxChildSumAsBranch = max(leftMaxPathAsBranch, rightMaxPathAsBranch)

    maxSumAsBranch = max(maxChildSumAsBranch + tree.value, tree.value)
    maxSumAsRootNode = max(rightMaxPathAsBranch + tree.value + leftMaxPathAsBranch, maxSumAsBranch)
    maxPath = max(leftMaxPath, rightMaxPath, maxSumAsRootNode)
    return (maxSumAsBranch, maxPath)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


if __name__ == '__main__':
    test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
    actual = maxPathSum(test)
    print(actual)
    assert actual == 18
