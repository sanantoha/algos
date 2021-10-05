
# O(n) time | O(n) space
def max_subset_sum_no_adjucent(array):
    if array is None or len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    dp = [0 for _ in range(len(array))]
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, len(array)):
       dp[i] = max(dp[i - 2] + array[i], dp[i - 1])

    return dp[-1]


# O(n) time | O(1) space
def max_subset_sum_no_adjucent1(array):
    if array is None or len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    fst = array[0]
    snd = max(array[0], array[1])

    for i in range(2, len(array)):
        snd, fst = max(fst + array[i], snd), snd

    return snd


if __name__ == '__main__':
    assert max_subset_sum_no_adjucent([75, 105, 120, 75, 90, 135]) == 330

    assert max_subset_sum_no_adjucent1([75, 105, 120, 75, 90, 135]) == 330
    print(max_subset_sum_no_adjucent1([75, 105, 120, 75, 90, 135]))
