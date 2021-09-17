
# O(n) time | O(1) space
def move_element_to_end(array, to_move):
    r = len(array) - 1
    j = r
    while r >= 0:
        curr = array[r]
        if curr == to_move:
            if r != j:
                swap(array, r, j)
            j -= 1
        r -= 1

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    print(move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
