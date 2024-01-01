

#
# https://leetcode.com/problems/find-pivot-index/
#
# Given an arrays of integers nums, calculate the pivot index of this arrays.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the arrays, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the arrays.
# Return the leftmost pivot index. If no such index exists, return -1.

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11


# O(n) time | O(1) space
def pivotIndex(arr):
    if not arr:
        return -1

    leftSum, rightSum = 0, sum(arr)

    for i in range(len(arr)):
        rightSum -= arr[i]

        if leftSum == rightSum:
            return i

        leftSum += arr[i]

    return -1


if __name__ == '__main__':

    actual = pivotIndex([1,7,3,6,5,6])
    print(actual)
    assert actual == 3
    assert pivotIndex([1,2,3]) == -1
    assert pivotIndex([2, 1, -1]) == 0