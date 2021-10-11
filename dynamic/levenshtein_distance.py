
"""
        a b c
      0 1 2 3
    y 1 1 2 3
    a 2 1 2 3
    b 3 2 1 2
    d 4 3 2 2
"""


# O(n * m) time | O(n * m) space
def levenshtein_distance(str1, str2):
    dp = [[x for x in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for row in range(len(dp)):
        dp[row][0] = row

    for row in range(1, len(dp)):
        for col in range(1, len(dp[row])):
            if str2[row - 1] == str1[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])

    return dp[-1][-1]


# O(n * m) time | O(min(n, m))
def levenshtein_distance1(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    even = [x for x in range(len(small) + 1)]
    odd = [None for _ in range(len(small) + 1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            current = odd
            prev = even
        else:
            current = even
            prev = odd
        current[0] = i

        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                current[j] = prev[j - 1]
            else:
                current[j] = 1 + min(prev[j - 1], prev[j], current[j - 1])

    return even[-1] if len(big) % 2 == 0 else odd[-1]


if __name__ == '__main__':
    assert levenshtein_distance("abc", "yabd") == 2
    assert levenshtein_distance1("abc", "yabd") == 2
