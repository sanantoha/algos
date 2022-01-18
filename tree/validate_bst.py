from tree.BST import BST


def validate_bst(tree):
    return validate(tree, float('-inf'), float('+inf'))


def validate(tree, min_val, max_val):
    if tree is None:
        return True

    if tree.value < min_val or tree.value >= max_val:
        return False

    return validate(tree.left, min_val, tree.value) and validate(tree.right, tree.value, max_val)


if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print(validate_bst(root))
    assert validate_bst(root)
