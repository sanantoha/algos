# O(n ^ 3) time | O(1) space (exclude return res)
def three_number_sum(arr, target):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    res.append([arr[i], arr[j], arr[k]])
    return res


# O(n ^ 2) time | O(1) space (exclude return res)
def three_number_sum1(arr, target):
    res = []
    arr.sort()

    for i in range(0, len(arr) - 1):
        if i > 0 and arr[i] == arr[i + 1]:
            continue

        l = i + 1
        r = len(arr) - 1
        while l < r:
            total_sum = arr[i] + arr[l] + arr[r]
            if total_sum == target:
                res.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
                while l < r and arr[l] == arr[l + 1]:
                    l += 1
                while l < r and arr[r] == arr[r - 1]:
                    r -= 1
            elif total_sum < target:
                l += 1
            else:
                r -= 1

    return res


if __name__ == '__main__':
    print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
    print(three_number_sum1([12, 3, 1, 2, -6, 5, -8, 6], 0))
