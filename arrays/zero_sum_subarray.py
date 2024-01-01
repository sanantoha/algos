
# O(n) time | O(n) space
def zeroSumSubarray(nums):
    sums = set([0])
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s in sums:
            return True
        sums.add(s)

    return False


if __name__ == '__main__':
    input = [4, 2, -1, -1, 3]
    expected = True
    actual = zeroSumSubarray(input)
    print(actual)
    assert actual == expected