from tree.BinaryTree import BinaryTree


# O(n) time | O(h) space
def evaluateExpressionTree(tree):
    if not tree:
        return 0
    if tree.value >= 0:
        return tree.value

    lv = evaluateExpressionTree(tree.left)
    rv = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return lv + rv
    if tree.value == -2:
        return lv - rv
    if tree.value == -3:
        return int(lv / rv)
    if tree.value == -4:
        return lv * rv

    return tree.value


if __name__ == '__main__':
    tree = BinaryTree(-1)
    tree.left = BinaryTree(-2)
    tree.left.left = BinaryTree(-4)
    tree.left.left.left = BinaryTree(2)
    tree.left.left.right = BinaryTree(3)
    tree.left.left.right = BinaryTree(2)

    tree.right = BinaryTree(-3)
    tree.right.left = BinaryTree(8)
    tree.right.right = BinaryTree(3)
    expected = 6
    actual = evaluateExpressionTree(tree)
    print(actual)
    assert actual == expected