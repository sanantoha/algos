
from BST import BST


# O(n ^ 2) time | O(n) space
def reconstruct_bst(pre_order_traversal_values):
    if not pre_order_traversal_values:
        return None

    root_val = pre_order_traversal_values[0]
    arr = pre_order_traversal_values[1:]
    bst = BST(root_val)
    bst.left = reconstruct_bst(list(filter(lambda x: x < root_val, arr)))
    bst.right = reconstruct_bst(list(filter(lambda x: x >= root_val, arr)))
    return bst


# O(n) time | O(n) space
def reconstruct_bst1(pre_order_traversal_values):
    tree_info = TreeInfo(0)
    return reconstruct_bst_from_range(float('-inf'), float('inf'), pre_order_traversal_values, tree_info)


def reconstruct_bst_from_range(lower_bound, upper_bound, pre_order_traversal_values, tree_info):
    if tree_info.root_idx == len(pre_order_traversal_values):
        return None

    root_value = pre_order_traversal_values[tree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        return None

    tree_info.root_idx += 1
    left_sub_tree = reconstruct_bst_from_range(lower_bound, root_value, pre_order_traversal_values, tree_info)
    right_sub_tree = reconstruct_bst_from_range(root_value, upper_bound, pre_order_traversal_values, tree_info)
    return BST(root_value, left_sub_tree, right_sub_tree)


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


def get_dfs_order(node, values):
    if node is None:
        return
    values.append(node.value)
    get_dfs_order(node.left, values)
    get_dfs_order(node.right, values)
    return values


if __name__ == '__main__':
    pre_order_traversal_values = [10, 4, 2, 1, 3, 17, 19, 18]
    tree = BST(10)
    tree.left = BST(4)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(17)
    tree.right.right = BST(19)
    tree.right.right.left = BST(18)
    expected = get_dfs_order(tree, [])

    actual = reconstruct_bst(pre_order_traversal_values)
    actual_dfs_order = get_dfs_order(actual, [])
    assert actual_dfs_order == expected

    actual1 = reconstruct_bst1(pre_order_traversal_values)
    actual_dfs_order1 = get_dfs_order(actual1, [])
    assert actual_dfs_order1 == expected
