from tree.BinaryTree import BinaryTree


# O(n) time | O(h) space - where n, h for smallest tree
def mergeBinaryTrees(tree1, tree2):
    if not tree1:
        return tree2
    if not tree2:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTreesIter(tree1.right, tree2.right)
    return tree1


# O(n) time | O(h) space - where n, h for smallest tree
def mergeBinaryTreesIter(tree1, tree2):
    if not tree1:
        return tree2

    stack1 = [tree1]
    stack2 = [tree2]

    while stack1:
        curr1 = stack1.pop()
        curr2 = stack2.pop()

        if not curr2:
            continue

        curr1.value += curr2.value

        if not curr1.left:
            curr1.left = curr2.left
        else:
            stack1.append(curr1.left)
            stack2.append(curr2.left)

        if not curr1.right:
            curr1.right = curr2.right
        else:
            stack1.append(curr1.right)
            stack2.append(curr2.right)

    return tree1


if __name__ == '__main__':
    tree1 = BinaryTree(1)
    tree1.left = BinaryTree(3)
    tree1.left.left = BinaryTree(7)
    tree1.left.right = BinaryTree(4)
    tree1.right = BinaryTree(2)

    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(5)
    tree2.left.left = BinaryTree(2)
    tree2.right = BinaryTree(9)
    tree2.right.left = BinaryTree(7)
    tree2.right.right = BinaryTree(6)

    actual = mergeBinaryTrees(tree1, tree2)
    assert actual.value == 2
    assert actual.left.value == 8
    assert actual.left.left.value == 9
    assert actual.left.right.value == 4
    assert actual.right.value == 11
    assert actual.right.left.value == 7
    assert actual.right.right.value == 6


    tree3 = BinaryTree(1)
    tree3.left = BinaryTree(3)
    tree3.left.left = BinaryTree(7)
    tree3.left.right = BinaryTree(4)
    tree3.right = BinaryTree(2)

    tree4 = BinaryTree(1)
    tree4.left = BinaryTree(5)
    tree4.left.left = BinaryTree(2)
    tree4.right = BinaryTree(9)
    tree4.right.left = BinaryTree(7)
    tree4.right.right = BinaryTree(6)

    actual = mergeBinaryTreesIter(tree3, tree4)
    assert actual.value == 2
    assert actual.left.value == 8
    assert actual.left.left.value == 9
    assert actual.left.right.value == 4
    assert actual.right.value == 11
    assert actual.right.left.value == 7
    assert actual.right.right.value == 6