
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)
    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)
    return False


def isDescendant(ancNode, descNode):
    curr = ancNode

    while curr:
        if curr.value == descNode.value:
            return True
        elif curr.value < descNode.value:
            curr = curr.right
        else:
            curr = curr.left

    return False


# ==================================================================

def validateThreeNodes1(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        if searchOne is None and searchTwo is None:
            return False
        if searchOne is nodeThree or searchTwo is nodeOne:
            return False

        if searchOne is nodeTwo:
            return isDescendant(nodeTwo, nodeThree)
        elif searchTwo is nodeTwo:
            return isDescendant(nodeTwo, nodeOne)

        if searchOne is not None:
            searchOne = searchOne.left if nodeTwo.value < searchOne.value else searchOne.right

        if searchTwo is not None:
            searchTwo = searchTwo.left if nodeTwo.value < searchTwo.value else searchTwo.right


if __name__ == '__main__':
    root = BST(5)
    root.left = BST(2)
    root.right = BST(7)
    root.left.left = BST(1)
    root.left.right = BST(4)
    root.right.left = BST(6)
    root.right.right = BST(8)
    root.left.left.left = BST(0)
    root.left.right.left = BST(3)

    nodeOne = root
    nodeTwo = root.left
    nodeThree = root.left.right.left
    expected = True
    actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
    print(actual)
    assert actual == expected

    actual = validateThreeNodes1(nodeOne, nodeTwo, nodeThree)
    print(actual)
    assert actual == expected
