
# O(n) time | O(1) space
def is_valid_subsequence(array, sequence):
    idx = 0
    for num in array:
        if num == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            break

    return idx == len(sequence)


# O(n) time | O(1) space
def is_valid_subsequence1(array, sequence):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(is_valid_subsequence(array, sequence))
    print(is_valid_subsequence1(array, sequence))
