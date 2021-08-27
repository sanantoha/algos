
# O(n ^ 2) time | O(1) space
def two_number_sum(array, target_sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []


# O(n) time | O(n) space
def two_number_sum1(array, target_sum):
    seen = set()
    for val in array:
        compensate = target_sum - val
        if compensate in seen:
            return [compensate, val]
        seen.add(val)

    return []


# O(n * log(n)) time | O(1) space
def two_number_sum2(array, target_sum):
    sorted_arr = sorted(array)
    left = 0
    right = len(sorted_arr) - 1

    while left < right:
        sum = sorted_arr[left] + sorted_arr[right]
        if sum == target_sum:
            return [sorted_arr[left], sorted_arr[right]]
        elif sum < target_sum:
            left += 1
        else:
            right -= 1

    return []


if __name__ == '__main__':
    print(two_number_sum2([3, 5, -4, 8, 11, 1, -1, 6], 10))