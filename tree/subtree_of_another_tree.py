from BinaryTree import BinaryTree


# O(n * m) time | O(n) space
def is_subtree(root, sub_root):

    stack = [root]

    while stack:
        curr = stack.pop()

        if not curr:
            continue

        if is_same_tree(curr, sub_root):
            return True

        stack.append(curr.right)
        stack.append(curr.left)

    return False


def is_same_tree(t1, t2):
    stack = [t1, t2]

    while stack:
        c1 = stack.pop()
        c2 = stack.pop()

        if not c1 and not c2:
            continue
        if not c1 or not c2:
            return False
        if c1.value != c2.value:
            return False

        stack.append(c1.left)
        stack.append(c2.left)
        stack.append(c1.right)
        stack.append(c2.right)

    return True


if __name__ == '__main__':
    root1 = BinaryTree(3)
    root1.left = BinaryTree(4)
    root1.left.left = BinaryTree(1)
    root1.left.right = BinaryTree(2)
    root1.right = BinaryTree(5)

    sub_tree = BinaryTree(4)
    sub_tree.left = BinaryTree(1)
    sub_tree.right = BinaryTree(2)

    res = is_subtree(root1, sub_tree)
    print(res)  # True
    assert res

    root2 = BinaryTree(3)
    root2.left = BinaryTree(4)
    root2.left.left = BinaryTree(1)
    root2.left.right = BinaryTree(2)
    root2.left.right.left = BinaryTree(0)
    root2.right = BinaryTree(5)

    res = is_subtree(root2, sub_tree)
    print(res)  # False
    assert not res

    root3 = BinaryTree(4)
    root3.left = BinaryTree(4)
    root3.left.left = BinaryTree(4)
    root3.left.left.left = BinaryTree(4)
    root3.left.left.left.left = BinaryTree(4)
    root3.left.left.left.left.left = BinaryTree(1)
    root3.left.left.left.left.right = BinaryTree(2)

    res = is_subtree(root3, sub_tree)
    print(res) # True
    assert res

