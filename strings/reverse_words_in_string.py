
def reverseWordsInString(string):
    chars = list(string)
    reverse(chars, 0, len(chars) - 1)

    startIdx = 0
    endIdx = startIdx
    while endIdx < len(chars):
        endIdx = startIdx
        while endIdx < len(chars) and chars[endIdx] != ' ':
            endIdx += 1
        reverse(chars, startIdx, endIdx - 1)
        startIdx = endIdx + 1

    return ''.join(chars)


def reverse(chars, l, r):
    while l < r:
        c = chars[l]
        chars[l] = chars[r]
        chars[r] = c
        l += 1
        r -= 1


if __name__ == '__main__':
    input = "AlgoExpert is the best!"
    expected = "best! the is AlgoExpert"
    actual = reverseWordsInString(input)
    print(actual)
    assert actual == expected