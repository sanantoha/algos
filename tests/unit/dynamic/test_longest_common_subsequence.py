import pytest

from dynamic.longest_common_subsequence import longestCommonSubsequence, longestCommonSubsequence1


TEST_CASE = [
    ("ZXVVYZW", "XKYKZPW", ["X", "Y", "Z", "W"]),
]


@pytest.mark.parametrize("s1, s2, exp", TEST_CASE)
def test_longestCommonSubsequence(s1, s2, exp):
    output = longestCommonSubsequence(s1, s2)
    print(output)
    assert output == exp


@pytest.mark.parametrize("s1, s2, exp", TEST_CASE)
def test_longestCommonSubsequence1(s1, s2, exp):
    output = longestCommonSubsequence1(s1, s2)
    print(output)
    assert output == exp