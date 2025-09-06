
# O(a1 * a2 + d * log(d)) time | O(a1 + a2) space
def relative_sort_array(arr1, arr2):
    cnt = [0 for _ in range(len(arr2))]

    missing = []

    for num in arr1:
        is_found = False
        for i in range(len(arr2)):
            if num == arr2[i]:
                is_found = True
                cnt[i] += 1

        if not is_found:
            missing.append(num)

    res = []
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            res.append(arr2[i])

    return res + sorted(missing)


# O(m + n * log(n)) time | O(n + m) space - where n = len(arr1), m = len(arr2)
def relative_sort_array_hashmap(arr1, arr2):
    count_map = {}
    remaining = []
    result = []
    # Initialize count map with relative order elements
    for value in arr2:
        count_map[value] = 0
    # Count occurrences of elements in target array
    for value in arr1:
        if value in count_map:
            count_map[value] += 1
        else:
            remaining.append(value)
    # Sort the remaining elements
    remaining.sort()
    # Add elements as per relative order
    for value in arr2:
        for _ in range(count_map[value]):
            result.append(value)
    # Add remaining elements
    result.extend(remaining)
    return result


# O(n+m+k) time | O(k) - where n = len(arr1), m = len(arr2), k - max(arr1)
def relative_sort_array_counting_sort(arr1, arr2):
    max_element = max(arr1)
    count = [0] * (max_element + 1)

    # Count occurrences of each element
    for element in arr1:
        count[element] += 1

    # Add elements as per relative order
    result = []
    for value in arr2:
        while count[value] > 0:
            result.append(value)
            count[value] -= 1

    # Add remaining elements in ascending order
    for num in range(max_element + 1):
        while count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result


if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    res = relative_sort_array(arr1, arr2)
    res1 = relative_sort_array_hashmap(arr1, arr2)
    res2 = relative_sort_array_counting_sort(arr1, arr2)

    print(res)
    print(res1)
    print(res2)
    assert res == [2,2,2,1,4,3,3,9,6,7,19]
    assert res1 == [2,2,2,1,4,3,3,9,6,7,19]
    assert res2 == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

    #==========================================

    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]

    res = relative_sort_array(arr1, arr2)
    res1 = relative_sort_array_hashmap(arr1, arr2)
    res2 = relative_sort_array_counting_sort(arr1, arr2)

    print(res)
    print(res1)
    print(res2)
    assert res == [22,28,8,6,17,44]
    assert res1 == [22, 28, 8, 6, 17, 44]
    assert res2 == [22, 28, 8, 6, 17, 44]
