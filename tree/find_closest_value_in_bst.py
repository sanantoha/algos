
# O(n) time | O(n) space
def find_closest_value_in_bst(tree, target):
    if tree is None:
        return float('inf')

    stack = [tree]
    min_diff = float('inf')
    min_value = tree.value

    while stack:
        curr = stack.pop()
        diff = abs(curr.value - target)
        if min_diff > diff:
            min_value = curr.value
            min_diff = diff

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return min_value


# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def find_closest_value_in_bst1(tree, target):
    return find_min_diff(tree, target, tree.value)


def find_min_diff(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return find_min_diff(tree.left, target, closest)
    elif target > tree.value:
        return find_min_diff(tree.right, target, closest)
    else:
        return closest


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_in_bst2(tree, target):

    closest = tree.value
    curr = tree

    while curr is not None:
        if abs(target - closest) > abs(target - curr.value):
            closest = curr.value
        if target < curr.value:
            curr = curr.left
        elif target > curr.value:
            curr = curr.right
        else:
            return curr.value

    return closest


if __name__ == '__main__':
    from BST import BST

    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    expected = 13

    print(find_closest_value_in_bst(root, 12))
    print(find_closest_value_in_bst1(root, 12))
    print(find_closest_value_in_bst2(root, 12))
