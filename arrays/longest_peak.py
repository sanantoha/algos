
# O(n) time | O(1) space
def longest_peak(array):
    max_peak = 0
    i = 1
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        l = i - 2
        while l >= 0 and array[l] < array[l + 1]:
            l -= 1

        r = i + 2
        while r < len(array) and array[r - 1] > array[r]:
            r += 1

        curr_peak = r - l - 1
        max_peak = max(max_peak, curr_peak)
        i = r

    return max_peak


if __name__ == '__main__':
    print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
