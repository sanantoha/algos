
# O(n) time | O(1) space
def kadanes_distance(array):
    if array is None or len(array) == 0:
        return 0

    max_sum = float('-inf')
    curr_sum = 0

    for num in array:
        curr_sum += num

        if max_sum < curr_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


# O(n) time | O(1) space
def kadanes_distance1(array):
    if array is None or len(array) == 0:
        return 0

    max_sum = array[0]
    curr_sum = array[0]

    for i in range(1, len(array)):
        curr_sum = max(array[i], curr_sum + array[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    assert kadanes_distance([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19
    assert kadanes_distance1([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19
