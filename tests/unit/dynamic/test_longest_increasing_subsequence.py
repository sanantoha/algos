from dynamic.longest_increasing_subsequence import longestIncreasingSubsequence
from dynamic.longest_increasing_subsequence import longestIncreasingSubsequence1


input = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]


def test_longest_increasing_subsequence():
    actual = longestIncreasingSubsequence(input)
    print(actual)
    assert actual == [-24, 2, 3, 5, 6, 35]


def test_longest_increasing_subsequence1():
    actual = longestIncreasingSubsequence1(input)
    print(actual)
    assert actual == [-24, 2, 3, 5, 6, 35]