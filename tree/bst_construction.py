
from BST import BST

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

    root.insert(12)
    assert(root.right.left.left.value == 12)

    root.remove(10)
    assert(not root.contains(10))
    assert(root.value == 12)

    assert(root.contains(15))

    root1 = BST(10)
    root1.left = BST(5)
    root1.left.left = BST(2)
    root1.left.left.left = BST(1)
    root1.left.right = BST(5)
    root1.right = BST(15)
    root1.right.left = BST(13)
    root1.right.left.right = BST(14)
    root1.right.right = BST(22)

    root1.insert_rec(12)
    assert (root1.right.left.left.value == 12)

    root1.remove_rec(10)
    assert (not root1.contains_rec(10))
    assert (root1.value == 12)

    assert (root1.contains_rec(15))