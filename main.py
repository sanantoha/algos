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
    "knapsack_problem.py"
]


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Node({self.val} {self.children})"


class Index:
    def __init__(self, i):
        self.idx = i

    def increment(self):
        self.idx += 1

class Codec:

    def serialize(self, root):

        def helper(root, index, res, parentIdx):

            if not root:
                return

            res.append(chr(index.idx + 48))
            res.append(chr(root.val + 48))
            parentIdx = chr(parentIdx + 48) if parentIdx else 'N'
            res.append(parentIdx)

            parentIdx = index.idx
            for child in root.children if root.children else []:
                index.increment()
                helper(child, index, res, parentIdx)

        if not root:
            return ""

        res = []
        helper(root, Index(1), res, None)
        return "".join(res)

    def deserialize(self, data):

        def helper(data):

            nodesMap = {}

            for i in range(0, len(data), 3):
                idx = ord(data[i]) - 48
                val = ord(data[i + 1]) - 48
                node = Node(val, [])
                nodesMap[idx] = node

            for i in range(3, len(data), 3):
                idx = ord(data[i]) - 48
                parentIdx = ord(data[i + 2]) - 48

                parent = nodesMap[parentIdx]
                parent.children.append(nodesMap[idx])

            return nodesMap[ord(data[0]) - 48]

        if not data:
            return None

        return helper(data)


class Codec1:

    def serialize(self, root):

        def helper(root, res):

            res.append(chr(root.val + 48))
            size = len(root.children) if root.children else 0
            res.append(chr(size + 48))

            for i in range(size):
                helper(root.children[i], res)


        if not root:
            return ""

        res = []
        helper(root, res)
        return "".join(res)

    def deserialize(self, data):

        def helper(data, index):

            val = ord(data[index.idx]) - 48
            node = Node(val, [])
            index.increment()
            size = ord(data[index.idx]) - 48

            for i in range(size):
                index.increment()
                node.children.append(helper(data, index))

            return node

        if not data:
            return None

        return helper(data, Index(0))


if __name__ == '__main__':
    remain = list(set(tasks) - set(tasks_done))
    random.shuffle(remain)
    print(remain)
    # root = Node(11, [Node(33, [Node(55), Node(6666)]), Node(22), Node(30)])
    # print(root)
    # codec = Codec()
    # str = codec.serialize(root)
    # print(str)
    #
    # tree = codec.deserialize(str)
    # print(tree)
    # # # #
    # codec1 = Codec1()
    # str = codec1.serialize(root)
    # print(str)
    #
    # tree = codec1.deserialize(str)
    # print(tree)