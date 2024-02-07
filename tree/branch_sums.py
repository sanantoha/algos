from tree.BinaryTree import BinaryTree


# O(n) time | O(h) space
def branch_sums(root):
    sums = []
    helper(root, 0, sums)
    return sums


def helper(root, curr_sum, sums):
    if root is None:
        return

    new_sum = curr_sum + root.value
    if root.left is None and root.right is None:
        sums.append(new_sum)
        return

    helper(root.left, new_sum, sums)
    helper(root.right, new_sum, sums)


# O(n) time | O(h) space
def branch_sums_iter(root):
    if not root:
        return []

    stack = [(root, 0)]
    res = []

    while stack:
        (curr, sum) = stack.pop()
        if not curr:
            continue

        sum += curr.value
        if not curr.left and not curr.right:
            res.append(sum)

        stack.append((curr.left, sum))
        stack.append((curr.right, sum))

    return res


if __name__ == '__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(sorted(branch_sums(tree)) == sorted([15, 16, 18, 10, 11]))

    print(sorted(branch_sums_iter(tree)) == sorted([15, 16, 18, 10, 11]))
