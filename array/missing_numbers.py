
# O(n) time | O(n) space
def missingNumbers(nums):
    ns = set(nums)

    res = []

    for i in range(1, len(nums) + 3):
        if i not in ns:
            res.append(i)

    return res


if __name__ == '__main__':
    input = [4, 5, 1, 3]
    expected = [2, 6]
    actual = missingNumbers(input)
    print(actual)
    assert actual == expected