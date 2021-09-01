from tree.BinaryTree import BinaryTree


# O(n) time | O(n) space
def branch_sums(root):
    sums = []
    calc_branch_sums(root, 0, sums)
    return sums


def calc_branch_sums(root, curr_sum, sums):
    if root is None:
        return

    new_sum = curr_sum + root.value
    if root.left is None and root.right is None:
        sums.append(new_sum)
        return

    calc_branch_sums(root.left, new_sum, sums)
    calc_branch_sums(root.right, new_sum, sums)


if __name__ == '__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(branch_sums(tree) == [15, 16, 18, 10, 11])
