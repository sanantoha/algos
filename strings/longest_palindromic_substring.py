
# O(n ^ 2) time | O(n) space
def longestPalindromicSubstring(string):
    if string is None or len(string) == 0:
        return ""

    currLongest = (0, 0)

    for i in range(len(string)):
        fst = getLongestPalindrom(string, i, i)
        snd = getLongestPalindrom(string, i, i + 1)
        longest = max(fst, snd, key=lambda x: x[1] - x[0])
        currLongest = max(currLongest, longest, key=lambda x: x[1] - x[0])

    return string[currLongest[0]: currLongest[1]]


def getLongestPalindrom(str, l, r):
    while l >= 0 and r < len(str):
        if str[l] != str[r]:
            break
        l -= 1
        r += 1

    return l + 1, r


if __name__ == '__main__':
    actual = longestPalindromicSubstring("abaxyzzyxf")
    print(actual)
    assert actual == "xyzzyx"
