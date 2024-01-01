
# O(n * log(n)) time | O(1) space
def largestRange(array):
    if array is None or len(array) == 0:
        return [-1, -1]

    array.sort()

    currLength = 0
    maxLength = 0
    start = array[0]
    currStart = array[0]
    end = array[0]

    for i in range(1, len(array)):
        if array[i - 1] == array[i]:
            continue
        elif array[i - 1] + 1 == array[i]:
            currLength += 1
        else:
            currStart = array[i]
            currLength = 1

        if maxLength < currLength:
            maxLength = currLength
            start = currStart
            end = array[i]

    return [start, end]


# O(n) time | O(n) space
def largestRange1(arr):
    if arr is None or len(arr) == 0:
        return [-1, -1]

    nums = {}
    for num in arr:
        nums[num] = True

    bestRange = [arr[0], arr[0]]
    maxLength = 0

    for num in arr:

        if not nums[num]:
            continue

        currLength = 1

        l = num - 1
        while l in nums:
            nums[l] = False
            currLength += 1
            l -= 1

        r = num + 1
        while r in nums:
            nums[r] = False
            currLength += 1
            r += 1

        if currLength > maxLength:
            maxLength = currLength
            bestRange = [l + 1, r - 1]

    return bestRange


if __name__ == '__main__':
    input = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    actual = largestRange(input)
    print(actual)
    assert actual == [0, 7]

    input = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    actual = largestRange(input)
    print(actual)
    assert actual == [10, 19]

    input = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    actual = largestRange1(input)
    print(actual)
    assert actual == [0, 7]

    input = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    actual = largestRange1(input)
    print(actual)
    assert actual == [10, 19]
