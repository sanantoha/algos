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
    'serialize_and_deserialize_n_ary_tree.py'
]

tasks_done = [
    "first_duplicate_value.py",
    "validate_tree_nodes.py",
    "number_of_ways_to_make_change.py",
    "valid_ip_addresses.py",
    "binary_tree_diameter.py",
    "longest_peak.py",
    "find_kth_largest_value_in_bst.py",
    "minimum_characters_for_words.py",
    "search_in_sorted_matrix.py",
    "first_non_repeating_character.py",
    "task_assignment.py",
    "phone_number_mnemonic.py",
    "minimum_waiting_time.py",
    "run_length_encoding.py",
    "tournament_winner.py",
    "non_constructible_changes.py",
    "find_closest_value_in_bst.py",
    "validate_subsequence.py",
    "two_number_sum.py"
]


def two_number_sum(arr, target):
    pass

def two_number_sum1(arr, target):
    pass

def two_number_sum2(arr, target):
    pass


if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)

    print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum1([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum2([3, 5, -4, 8, 11, 1, -1, 6], 10))
