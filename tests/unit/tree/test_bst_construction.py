from tree.BST import BST


def test_bst_construction():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert(12)
    assert (root.right.left.left.value == 12)

    root.remove(10)
    assert (not root.contains(10))
    assert (root.value == 12)

    assert (root.contains(15))


def test_bst_construction_rec():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert_rec(12)
    assert (root.right.left.left.value == 12)

    root.remove_rec(10)
    assert (not root.contains_rec(10))
    assert (root.value == 12)

    assert (root.contains_rec(15))