import collections
import random

tasks = [
    'apartment_hunting.py',
    'array_of_products.py',
    'first_duplicate_value.py',
    'four_number_sum.py',
    'largest_range.py',
    'merge_overlapping_intervals.py',
    'longest_peak.py',
    'min_rewards.py',
    'minimum_waiting_time.py',
    'move_element_to_end.py',
    'monotonic_array.py',
    'non_constructible_changes.py',
    'smallest_difference.py',
    'sorted_squared_array.py',
    'spiral_matrix_traverse.py',
    'subarray_sort.py',
    'three_number_sum.py',
    'tournament_winner.py',
    'two_number_sum.py',
    'valid_starting_city.py',
    'validate_subsequence.py',
    'zigzag_traverse.py',
    'kadanes_distance.py',
    'levenshtein_distance.py',
    'longest_common_subsequence.py',
    'longest_increasing_subsequence.py',
    'max_subset_sum_no_adjucent.py',
    'max_sum_increasing_subsequence.py',
    'min_number_of_coins_for_change.py',
    'numbers_of_ways_to_traverse_graph.py',
    'number_of_ways_to_make_change.py',
    'a_star_algorithm.py',
    'breadth_first_search.py',
    'cycle_in_graph.py',
    'depth_first_search.py',
    'get_youngest_common_ancestor.py',
    'minimum_passes_of_matrix.py',
    'river_sizes.py',
    'remove_islands.py',
    'single_cycle_check.py',
    'min_heap_construction.py',
    'linked_list_construction.py',
    'remove_duplicates_from_linkedlist.py',
    'remove_kth_node_from_end.py',
    'sum_of_linked_lists.py',
    'get_nth_fib.py',
    'permutations.py',
    'phone_number_mnemonic.py',
    'powerset.py',
    'product_sum.py',
    'staircase_traversal.py',
    'binary_search.py',
    'find_three_largest_numbers.py',
    'search_in_sorted_matrix.py',
    'bubble_sort.py',
    'insertion_sort.py',
    'class_photos.py',
    'selection_sort.py',
    'tandem_bicycle.py',
    'task_assignment.py',
    'three_number_sort.py',
    'balanced_brackets.py',
    'min_max_stack_construction.py',
    'next_greater_element.py',
    'sort_stack.py',
    'sunset_views.py',
    'first_non_repeating_character.py',
    'caesar_cipher_encryptor.py',
    'generate_document.py',
    'group_anagrams.py',
    'longest_palindromic_substring.py',
    'minimum_characters_for_words.py',
    'palindrom_check.py',
    'reverse_words_in_string.py',
    'run_length_encoding.py',
    'valid_ip_addresses.py',
    'binary_tree_diameter.py',
    'branch_sums.py',
    'bst_construction.py',
    'bst_traversal.py',
    'find_closest_value_in_bst.py',
    'find_nodes_distance_k.py',
    'find_kth_largest_value_in_bst.py',
    'find_successor.py',
    'height_balanced_binary_tree.py',
    'invert_binary_tree.py',
    'max_sum_in_binary_tree.py',
    'min_height_bst.py',
    'node_depths.py',
    'reconstruct_bst.py',
    'same_bsts.py',
    'validate_bst.py',
    'validate_tree_nodes.py',
    'suffix_trie_construction.py',
    'water_area.py',
    'knapsack_problem.py',
    'disk_stacking.py',
    'word_ladder.py',
    'word_ladder_ii.py',
    'serialize_and_deserialize_n_ary_tree.py',
    'all_paths_source_target.py',
    'semordinal.py',
    'merge_binary_trees.py',
    'stable_internships.py',
    'unique_pathsIII.py',
    'zero_sum_subarray.py',
    'merging_linked_lists.py',
    'simmetrical_tree.py',
    'union_find.py',
    'kruskals_algorithm.py',
    'one_edit.py',
    'two_colorable.py',
    'evaluate_expression_tree.py',
    'find_pivot_index.py',
    'middle_node.py',
    'transpose_matrix.py',
    'common_characters.py',
    'best_digits.py',
    'best_seats.py'
]

tasks_done = [
    "minimum_characters_for_words.py",
    "bubble_sort.py"
    "three_number_sum.py",
    "numbers_of_ways_to_traverse_graph.py",
    "tandem_bicycle.py",
    "product_sum.py",
    "remove_duplicates_from_linkedlist.py",
    "smallest_difference.py",
    "get_youngest_common_ancestor.py",
    "min_rewards.py",
    "palindrom_check.py",
    "two_number_sum.py",
    "max_subset_sum_no_adjucent.py",
    "get_nth_fib.py",
    "generate_document.py",
    "min_number_of_coins_for_change.py",
    "bst_traversal.py",
    "valid_ip_addresses.py",
    "word_ladder.py",
    "permutations.py",
    "sunset_views.py",
    "find_kth_largest_value_in_bst.py",
    "binary_tree_diameter.py",
    "find_closest_value_in_bst.py",
    "find_three_largest_numbers.py",
    "insertion_sort.py",
    "number_of_ways_to_make_change.py",
    "merge_binary_trees.py",
    "phone_number_mnemonic.py",
    "merge_overlapping_intervals.py",
    "bubble_sort.py",
    "height_balanced_binary_tree.py",
    "valid_starting_city.py",
    "move_element_to_end.py",
    "minimum_passes_of_matrix.py",
    "group_anagrams.py",
    "remove_kth_node_from_end.py",
    "unique_pathsIII.py",
    "two_colorable.py",
    "word_ladder_ii.py",
    "minimum_waiting_time.py",
    "spiral_matrix_traverse.py",
    "single_cycle_check.py",
    "depth_first_search.py",
    "union_find.py",
    "search_in_sorted_matrix.py",
    "three_number_sum.py",
    "binary_search.py",
    "subarray_sort.py",
    "invert_binary_tree.py",
    "three_number_sort.py",
    "caesar_cipher_encryptor.py",
    "suffix_trie_construction.py",
    "a_star_algorithm.py",
    "simmetrical_tree.py",
    "max_sum_increasing_subsequence.py",
    "same_bsts.py",
    "river_sizes.py",
    "find_successor.py",
    "zero_sum_subarray.py",
    "breadth_first_search.py",
    "longest_palindromic_substring.py",
    "validate_subsequence.py",
    "largest_range.py",
    "longest_peak.py",
    "cycle_in_graph.py",
    "non_constructible_changes.py",
    "merging_linked_lists.py",
    "balanced_brackets.py",
    "kadanes_distance.py",
    "validate_tree_nodes.py",
    "sorted_squared_array.py",
    "one_edit.py",
    "next_greater_element.py",
    "branch_sums.py",
    "validate_bst.py",
    "semordinal.py",
    "longest_increasing_subsequence.py",
    "first_non_repeating_character.py",
    "first_duplicate_value.py",
    "powerset.py",
    "array_of_products.py",
    "reverse_words_in_string.py",
    "max_sum_in_binary_tree.py",
    "all_paths_source_target.py",
    "class_photos.pyf",
    "find_pivot_index.py",
    "tournament_winner.py",
    "transpose_matrix.py",
    "min_heap_construction.py",
    "common_characters.py",
    "water_area.py",
    "remove_islands.py",
    "serialize_and_deserialize_n_ary_tree.py",
    "selection_sort.py",
    "levenshtein_distance.py",
    "evaluate_expression_tree.py",
    "reconstruct_bst.py"
]


from tree.BST import BST

def reconstruct_bst(pre_order_traversal_values):
    pass

def reconstruct_bst1(pre_order_traversal_values):
    pass


def get_dfs_order(node, values):
    if node is None:
        return
    values.append(node.value)
    get_dfs_order(node.left, values)
    get_dfs_order(node.right, values)
    return values


if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)

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
