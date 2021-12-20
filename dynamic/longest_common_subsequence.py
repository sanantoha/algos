
# O(n * m * min(n, m)) time | O(n * m * min(n, m))
def longestCommonSubsequence(str1, str2):
    if str1 is None or str2 is None:
        return []

    lcs = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str1[j - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)

    return lcs[-1][-1]


# O(n * m) time | O(n * m) space
def longestCommonSubsequence1(str1, str2):
    lcs = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str1[j - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

    return buildSequence(lcs)


def buildSequence(lcs):
    seq = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        curr = lcs[i][j]
        if curr[0] is not None:
            seq.append(curr[0])
        i = curr[2]
        j = curr[3]

    return list(reversed(seq))


if __name__ == '__main__':
    output = longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
    print(output)
    assert output == ["X", "Y", "Z", "W"]


    output = longestCommonSubsequence1("ZXVVYZW", "XKYKZPW")
    print(output)
    assert output == ["X", "Y", "Z", "W"]