
# O(n * log(m) + m * log(n)) time | O(1) space
def smallest_difference(arr_one, arr_two):
    arr_one.sort()
    arr_two.sort()

    res = []
    idx_one, idx_two = 0, 0
    min_diff = float('inf')
    while idx_one < len(arr_one) and idx_two < len(arr_two):
        curr_diff = abs(arr_one[idx_one] - arr_two[idx_two])

        if min_diff > curr_diff:
            min_diff = curr_diff
            res = [arr_one[idx_one], arr_two[idx_two]]

        if curr_diff == 0:
            return res
        elif arr_one[idx_one] < arr_two[idx_two]:
            idx_one += 1
        else:
            idx_two += 1

    return res


if __name__ == '__main__':
    print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))  # [28, 26]
