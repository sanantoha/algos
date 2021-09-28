
from BST import BST


def pre_order_traverse(tree, arr):
    if tree is None:
        return arr

    arr.append(tree.value)
    arr = pre_order_traverse(tree.left, arr)
    return pre_order_traverse(tree.right, arr)


def pre_order_traverse_iter(tree, arr):
    if tree is None:
        return arr

    stack = [tree]
    while stack:
        curr = stack.pop()
        arr.append(curr.value)

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return arr


def in_order_traverse(tree, arr):
    if tree is None:
        return arr

    arr = in_order_traverse(tree.left, arr)
    arr.append(tree.value)
    return in_order_traverse(tree.right, arr)


def in_order_traverse_iter(tree, arr):
    if tree is None:
        return arr

    stack = []
    curr = tree
    while stack or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        arr.append(curr.value)

        curr = curr.right

    return arr


def post_order_traverse(tree, arr):
    if tree is None:
        return arr

    arr = post_order_traverse(tree.left, arr)
    arr = post_order_traverse(tree.right, arr)
    arr.append(tree.value)
    return arr


def post_order_traverse_iter(tree, arr):
    if tree is None:
        return arr

    fst = []
    snd = []
    fst.append(tree)

    while fst:
        curr = fst.pop()
        snd.append(curr)

        if curr.left is not None:
            fst.append(curr.left)
        if curr.right is not None:
            fst.append(curr.right)

    while snd:
        arr.append(snd.pop().value)

    return arr


if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.right = BST(22)

    in_order = [1, 2, 5, 5, 10, 15, 22]
    pre_order = [10, 5, 2, 1, 5, 15, 22]
    post_order = [1, 2, 5, 5, 22, 15, 10]

    assert pre_order_traverse(root, []) == pre_order
    assert pre_order_traverse_iter(root, []) == pre_order

    assert in_order_traverse(root, []) == in_order
    assert in_order_traverse_iter(root, []) == in_order

    assert post_order_traverse(root, []) == post_order
    assert post_order_traverse_iter(root, []) == post_order
