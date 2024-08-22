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
    'lagest_island.py',
]

tasks_done = [
    'suffix_trie_construction.py',
    'find_pivot_index.py',
    'subarray_sort.py',
    'longest_palindromic_substring.py',
    'stable_internships.py',
    'search_in_sorted_matrix.py',
    'caesar_cipher_encryptor.py',
    'branch_sums.py',
    'numbers_of_ways_to_traverse_graph.py',
    'min_height_bst.py',
    'class_photos.py',
    'merging_linked_lists.py',
    'array_of_products.py',
    'one_edit.py',
    'longest_common_subsequence.py',
    'bubble_sort.py',
    'find_closest_value_in_bst.py',
    'find_successor.py',
    'min_max_stack_construction.py',
    'minimum_passes_of_matrix.py',
    'semordinal.py',
    'disk_stacking.py',
    'balanced_brackets.py',
    'min_number_of_coins_for_change.py',
    'invert_binary_tree.py',
    'knapsack_problem.py',
    'cycle_in_graph.py',
    'longest_peak.py',
    'product_sum.py',
    'height_balanced_binary_tree.py',
    'bst_traversal.py',
    'largest_range.py',
    'find_kth_largest_value_in_bst.py',
    'two_number_sum.py',
    'max_sum_in_binary_tree.py',
    'all_paths_source_target.py',
    'next_greater_element.py',
    'palindrom_check.py',
    'sum_of_linked_lists.py',
    'tournament_winner.py',
    'water_area.py',
    'missing_numbers.py',
    'minimum_characters_for_words.py',
    'task_assignment.py',
    'binary_tree_diameter.py',
    'first_duplicate_value.py',
    'find_nodes_distance_k.py',
    'move_element_to_end.py',
    'selection_sort.py',
    'evaluate_expression_tree.py',
    'validate_subsequence.py',
    'transpose_matrix.py',
    'simmetrical_tree.py',
    'validate_tree_nodes.py',
    'sorted_squared_array.py',
    'median_of_two_sorted_arrays.py',
    'majority_element.py',
    'phone_number_mnemonic.py',
    'spiral_matrix_traverse.py',
    'valid_starting_city.py',
    'merge_overlapping_intervals.py',
    'minimum_waiting_time.py',
    'generate_document.py',
    'tandem_bicycle.py',
    'staircase_traversal.py',
    'apartment_hunting.py',
    'best_digits.py',
    'run_length_encoding.py',
    'remove_duplicates_from_linkedlist.py',
    'serialize_and_deserialize_n_ary_tree.py',
    'insertion_sort.py',
    'optimal_freelancing.py',
    'two_colorable.py',
    'breadth_first_search.py',
    'best_seats.py',
    'node_depths.py',
    'word_ladder.py',
    'single_cycle_check.py',
    'permutations.py',
    'union_find.py',
    'number_of_ways_to_make_change.py',
    'three_number_sort.py',
    'lagest_island.py',
    'reverse_polish_notation.py',
    'three_number_sum.py',
    'get_nth_fib.py',
    'monotonic_array.py',
    'smallest_difference.py',
    'reverse_words_in_string.py',
    'remove_islands.py',
    'validate_bst.py',
    'group_anagrams.py',
    'max_subset_sum_no_adjucent.py',
    'a_star_algorithm.py',
    'sort_stack.py',
    'longest_increasing_subsequence.py',
    'powerset.py',
    'kruskals_algorithm.py',
    'river_sizes.py',
    'sunset_views.py',
    'depth_first_search.py',
    'four_number_sum.py',
    'zero_sum_subarray.py',
    'number_of_islands.py',
    'find_three_largest_numbers.py',
    'zigzag_traverse.py',
    'common_characters.py',
    'first_non_repeating_character.py',
    'middle_node.py',
    'valid_ip_addresses.py',
    'same_bsts.py',
    'min_rewards.py',
    'get_youngest_common_ancestor.py',
    'unique_pathsIII.py',
    'kadanes_distance.py',
    'non_constructible_changes.py',
    'word_ladder_ii.py',
    'levenshtein_distance.py',
    'blackjack_probability.py',
    'merge_binary_trees.py',
    'remove_kth_node_from_end.py',
    'reconstruct_bst.py',
    'binary_search.py',
    'min_heap_construction.py',
    'max_sum_increasing_subsequence.py',
    'linked_list_construction.py'
]

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        pass

    def remove(self, node):
        pass

    def containsNodeWithValue(self, value):
        return False


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)

    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    # three2 = Node(3)
    # three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    linkedList.setHead(one)
    linkedList.insertAfter(one, two)
    linkedList.insertAfter(two, three)
    linkedList.insertAfter(three, four)
    linkedList.insertAfter(four, five)
    linkedList.insertAfter(five, six)
    seven = Node(7)
    linkedList.insertAfter(six, seven)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(7, one)
    print(getNodeValuesHeadToTail(linkedList))
    linkedList.insertAtPosition(1, one)
    print(getNodeValuesHeadToTail(linkedList))
    linkedList.insertAtPosition(2, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(3, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(4, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(5, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(6, one)
    print(getNodeValuesHeadToTail(linkedList))
