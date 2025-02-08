
# O(n * l) time | O(c) time - l is the length of the longest string, c - unique characters across the strings
def commonCharacters(strings):
    if not strings:
        return []
    map = {}
    for word in strings:
        mapForOneWord = {}
        for c in word:
            if c not in mapForOneWord:
                mapForOneWord[c] = 1

        for k, v in mapForOneWord.items():
            nv = map.get(k, 0) + v
            map[k] = nv

    res = []
    l = len(strings)
    for k, v in map.items():
        if v == l:
            res.append(k)

    return res


if __name__ == '__main__':
    input = ["abc", "bcdc", "bad"]
    expected = ["b", "c"]
    actual = commonCharacters(input)
    actual.sort()
    print(actual)
    assert actual == expected
