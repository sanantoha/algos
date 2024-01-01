
# O(log(min(a1, a2))) time | O(1) space
def medianOfTwoSortedArrays(arr1, arr2):
    if not arr1:
        return median(arr2)
    if not arr2:
        return median(arr1)

    l1 = len(arr1)
    l2 = len(arr2)
    if l1 > l2:
        return medianOfTwoSortedArrays(arr2, arr1)

    l = 0
    r = l1

    while l <= r:
        m1 = (l + r) // 2
        m2 = (l1 + l2 + 1) // 2 - m1

        leftMax1 = float('-inf') if m1 == 0 else arr1[m1 - 1]
        rightMin1 = float('inf') if m1 == l1 else arr1[m1]

        leftMax2 = float('-inf') if m2 == 0 else arr2[m2 - 1]
        rightMin2 = float('inf') if m2 == l2 else arr2[m2]

        if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
            if (l1 + l2) % 2 == 0:
                return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2
            else:
                return max(leftMax1, leftMax2)
        elif leftMax1 > rightMin2:
            r = m1 - 1
        else:
            l = m1 + 1

    return -1


def median(arr):
    if not arr:
        return -1

    l = len(arr)
    m = l // 2
    if l % 2 == 0:
        return (arr[m] + arr[m - 1]) / 2
    else:
        return arr[m]


if __name__ == '__main__':
    arrayOne = [1, 3, 4, 5]
    arrayTwo = [2, 3, 6, 7]
    actual = medianOfTwoSortedArrays(arrayOne, arrayTwo)
    print(actual)
    assert actual == 3.5

    actual = medianOfTwoSortedArrays([6, 7, 8, 9], [1, 3, 4, 5])
    print(actual)
    assert actual == 5.5
