
from BinaryTree import BinaryTree

# O(n) time | O(h) space
def symmetricalTreeRec(tree):
    return helper(tree.left, tree.right)


def helper(l, r):
    if not l and not r:
        return True
    elif not l or not r:
        return False

    return l.value == r.value and helper(l.left, r.right) and helper(l.right, r.left)

# O(n) time | O(h) space
def symmetricalTree(tree):
    if not tree:
        return True

    stack = [tree.left, tree.right]

    while stack:
        curr1 = stack.pop()
        curr2 = stack.pop()

        if not curr1 and not curr2:
            continue

        if not curr1 or not curr2:
            return False
        if curr1.value != curr2.value:
            return False

        stack.append(curr1.left)
        stack.append(curr2.right)

        stack.append(curr1.right)
        stack.append(curr2.left)

    return True

if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.left = BinaryTree(5)
    tree.right = BinaryTree(5)
    tree.left.left = BinaryTree(7)
    tree.left.right = BinaryTree(9)
    tree.right.left = BinaryTree(9)
    tree.right.right = BinaryTree(7)

    expected = True

    actual = symmetricalTreeRec(tree)
    print(actual)
    assert actual == expected

    actual = symmetricalTree(tree)
    print(actual)
    assert actual == expected