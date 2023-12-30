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
    'best_seats.py',
    'missing_numbers.py',
    'reverse_polish_notation.py',
    'majority_element.py',
    'optimal_freelancing.py',
    'median_of_two_sorted_arrays.py',
    'blackjack_probability.py',
    'number_of_islands.py',
    'lagest_island.py'
]

tasks_done = [
    'depth_first_search.py',
    'min_heap_construction.py',
    'min_number_of_coins_for_change.py',
    'minimum_waiting_time.py',
    'suffix_trie_construction.py',
    'max_sum_in_binary_tree.py',
    'selection_sort.py',
    'binary_tree_diameter.py',
    'smallest_difference.py',
    'river_sizes.py',
    'two_number_sum.py',
    'validate_subsequence.py',
    'find_kth_largest_value_in_bst.py',
    'kadanes_distance.py',
    'number_of_ways_to_make_change.py',
    'node_depths.py',
    'breadth_first_search.py',
    'minimum_passes_of_matrix.py',
    'unique_pathsIII.py',
    'first_non_repeating_character.py',
    'reverse_polish_notation.py',
    'minimum_characters_for_words.py',
    'task_assignment.py',
    'first_duplicate_value.py',
    'merge_binary_trees.py',
    'insertion_sort.py',
    'validate_tree_nodes.py',
    'generate_document.py',
    'permutations.py',
    'remove_kth_node_from_end.py',
    'valid_starting_city.py',
    'sort_stack.py',
    'middle_node.py',
    'monotonic_array.py',
    'find_pivot_index.py',
    'longest_palindromic_substring.py',
    'get_youngest_common_ancestor.py',
    'three_number_sort.py',
    'blackjack_probability.py',
    'best_digits.py',
    'subarray_sort.py',
    'non_constructible_changes.py',
    'semordinal.py',
    'find_successor.py',
    'single_cycle_check.py',
    'caesar_cipher_encryptor.py',
    'one_edit.py',
    'lagest_island.py',
    'union_find.py',
    'reverse_words_in_string.py',
    'max_subset_sum_no_adjucent.py',
    'find_three_largest_numbers.py',
    'staircase_traversal.py',
    'merge_overlapping_intervals.py',
    'class_photos.py',
    'number_of_islands.py',
    'sorted_squared_array.py',
    'balanced_brackets.py',
    'valid_ip_addresses.py',
    'palindrom_check.py',
    'longest_increasing_subsequence.py',
    'transpose_matrix.py',
    'bubble_sort.py',
    'levenshtein_distance.py',
    'min_rewards.py',
    'remove_duplicates_from_linkedlist.py',
    'tandem_bicycle.py',
    'numbers_of_ways_to_traverse_graph.py',
    'array_of_products.py',
    'tournament_winner.py',
    'move_element_to_end.py',
    'invert_binary_tree.py',
    'search_in_sorted_matrix.py',
    'optimal_freelancing.py',
    'zigzag_traverse.py'
    'binary_search.py',
    'water_area.py',
    'powerset.py',
    'best_seats.py',
    'word_ladder_ii.py',
    'group_anagrams.py',
    'longest_common_subsequence.py',
    'knapsack_problem.py',
    'bst_construction.py'
]

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def insert_rec(self, value):
        return self


    def insert(self, value):
        return self


    def contains_rec(self, value):
        return False


    def contains(self, value):
        return False


    def remove_rec(self, value, parent=None):
        return self


    def remove(self, value, parent=None):
        return self


if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)

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