
from BST import BST


def find_kth_largest_value_in_bst(tree, k):
    if tree is None:
        return -1

    stack = []
    curr = tree
    while tree or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.right

        curr = stack.pop()
        if k - 1 <= 0:
            return curr.value
        k -= 1

        curr = curr.left

    return -1


if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3
    expected = 17
    actual = find_kth_largest_value_in_bst(root, k)
    print(actual)
    assert actual == expected
