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
    "validate_bst.py",
    "remove_islands.py",
    "permutations.py",
    "number_of_ways_to_make_change.py",
    "search_in_sorted_matrix.py",
    "largest_range.py",
    "minimum_characters_for_words.py",
    "cycle_in_graph.py",
    "tournament_winner.py",
    "knapsack_problem.py",
    "balanced_brackets.py"
    "task_assignment.py",
    "bubble_sort.py",
    "depth_first_search.py",
    "min_height_bst.py",
    "reverse_words_in_string.py",
    "word_ladder.py",
    "serialize_and_deserialize_n_ary_tree.py",
    "two_number_sum.py",
    "group_anagrams.py",
    "max_sum_increasing_subsequence.py",
    "non_constructible_changes.py",
    "kadanes_distance.py",
    "find_closest_value_in_bst.py",
    "find_successor.py",
    "validate_subsequence.py",
    "phone_number_mnemonic.py",
    "node_depths.py",
    "three_number_sum.py",
    "remove_duplicates_from_linkedlist.py",
    "task_assignment.py",
    "binary_tree_diameter.py",
    "linked_list_construction.py",
    "invert_binary_tree.py",
    "monotonic_array.py",
    "binary_search.py",
    "max_subset_sum_no_adjucent.py",
    "water_area.py",
    "bst_traversal.py",
    "find_kth_largest_value_in_bst.py",
    "powerset.py",
    "caesar_cipher_encryptor.py",
    "min_heap_construction.py",
    "find_nodes_distance_k.py",
    "longest_common_subsequence.py",
    "move_element_to_end.py",
    "class_photos.py",
    "next_greater_element.py",
    "first_duplicate_value.py",
    "max_sum_in_binary_tree.py",
    "tandem_bicycle.py",
    "valid_ip_addresses.py",
    "min_max_stack_construction.py",
    "validate_tree_nodes.py",
    "sort_stack.py",
    "longest_palindromic_substring.py",
    "reconstruct_bst.py",
    "river_sizes.py",
    "balanced_brackets.py",
    "numbers_of_ways_to_traverse_graph.py"
]

# O(2 ^ (w * h)) time | O(w + h) space
def numbers_of_ways_to_traverse_graph_rec(width, height):
    if width == 1 or height == 1:
        return 1

    return numbers_of_ways_to_traverse_graph_rec(width - 1, height) + \
           numbers_of_ways_to_traverse_graph_rec(width, height - 1)

# O(w * h) time | O(w * h) space
def numbers_of_ways_to_traverse_graph(width, height):

    dp = [[1 for _ in range(width)] for _ in range(height)]

    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[height - 1][width - 1]


def numbers_of_ways_to_traverse_graph_math(width, height):
    x = width - 1
    y = height - 1
    return factorial(x + y) // (factorial(x) * factorial(y))

def factorial(n):
    if n == 0:
        return 1

    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    pass


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes

if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)

    ll1 = LinkedList(2).addMany([4, 7, 1])
    ll2 = LinkedList(9).addMany([4, 5])
    expected = LinkedList(1).addMany([9, 2, 2])
    actual = sumOfLinkedLists(ll1, ll2)
    print(getNodesInArray(actual))
    assert getNodesInArray(actual) == getNodesInArray(expected)

