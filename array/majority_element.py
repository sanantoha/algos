
# O(n) time | O(1) space
def majorityElement(arr):
    if not arr:
        return None

    curr = arr[0]
    count = 1

    for i in range(1, len(arr)):
        num = arr[i]

        if curr == num:
            count += 1
        elif count == 0:
            curr = num
        else:
            count -= 1

    return curr


if __name__ == '__main__':
    input = [1, 2, 3, 2, 2, 1, 2]
    expected = 2
    actual = majorityElement(input)
    print(actual)
    assert actual == expected

    input = [3, 3, 1]
    expected = 3
    actual = majorityElement(input)
    print(actual)
    assert actual == expected