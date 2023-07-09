
# O(n) time | O(n) space
def missingNumbers(nums):
    ns = set(nums)

    res = []

    for i in range(1, len(nums) + 3):
        if i not in ns:
            res.append(i)

    return res

# O(n) time | O(1) space
def missingNumbers1(nums):
    nums.append(1)
    nums.append(1)

    for i in range(len(nums) - 2):
        num = nums[i]
        nums[num - 1] *= -1

    res = []
    for i in range(len(nums)):
        num = nums[i]
        if num > 0:
            res.append(i + 1)

    return res


if __name__ == '__main__':
    input = [4, 5, 1, 3]
    expected = [2, 6]
    actual = missingNumbers(input)
    print(actual)
    assert actual == expected

    actual = missingNumbers1(input)
    print(actual)
    assert actual == expected