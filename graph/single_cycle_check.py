
# O(n) time | O(1) space
def single_cycle_check(array):
    if array is None or len(array) == 0:
        return False

    curr_idx = 0
    num_element_visited = 0

    while num_element_visited < len(array):
        if num_element_visited > 0 and curr_idx == 0:
            return False
        num_element_visited += 1
        curr_idx = get_next_index(array, curr_idx)

    return curr_idx == 0


def get_next_index(array, idx):
    move = array[idx]
    next_idx = (idx + move) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


if __name__ == '__main__':
    array = [2, 3, 1, -4, -4, 2]
    print(single_cycle_check(array))
    assert single_cycle_check(array)
