
# O(4 ^ n * n) time | O(4 ^ n * n) space
def phoneNumberMnemonics(phoneNumber):
    res = []
    letters = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    backtrack(phoneNumber, letters, 0, "", res)
    return res


def backtrack(phoneNumber, letters, idx, ans, res):
    if idx == len(phoneNumber):
        res.append(ans)
        return

    digit = int(phoneNumber[idx])
    letter = letters[digit]
    for c in letter:
        backtrack(phoneNumber, letters, idx + 1, ans + c, res)


if __name__ == '__main__':
    phoneNumber = "1905"
    expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
    actual = phoneNumberMnemonics(phoneNumber)
    print(actual)
    assert actual == expected