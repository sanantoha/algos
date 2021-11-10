
# O(n ^ 2) time | O(n) space
def nextGreaterElement(array):
    if array is None or len(array) == 0:
        return []

    res = []

    for i in range(len(array)):
        res.append(next(array, i))

    return res


def next(array, idx):
    i = idx
    k = idx + 1
    while True:
        j = k % len(array)
        if array[i] < array[j]:
            return array[j]
        elif k == 2 * len(array):
            return -1
        else:
            k += 1


# O(n) time | O(n) time
def nextGreaterElement1(array):
    if array is None or len(array) == 0:
        return []

    res = [-1 for _ in range(len(array))]
    stack = []

    for i in range(2 * len(array)):
        currIdx = i % len(array)

        while stack and array[stack[len(stack) - 1]] < array[currIdx]:
            top = stack.pop()
            res[top] = array[currIdx]

        stack.append(currIdx)

    return res


# O(n) time | O(n) space
def nextGreaterElement2(array):
    if array is None or len(array) == 0:
        return []

    stack = []
    res = [-1] * len(array)

    for i in reversed(range(2 * len(array) - 1)):
        currIdx = i % len(array)

        while stack:
            if stack[len(stack) - 1] <= array[currIdx]:
                stack.pop()
            else:
                res[currIdx] = stack[len(stack) - 1]
                break

        stack.append(array[currIdx])

    return res


if __name__ == '__main__':
    input = [2, 5, -3, -4, 6, 7, 2]
    expected = [5, 6, 6, 6, 7, -1, 5]
    actual = nextGreaterElement(input)
    print(actual)
    assert actual == expected

    actual = nextGreaterElement1(input)
    print(actual)
    assert actual == expected

    actual = nextGreaterElement2(input)
    print(actual)
    assert actual == expected
