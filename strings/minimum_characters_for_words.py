
# O(n * l) time | O(c) space
# where - n is the number of words
# l - is the length of the longest word
# c - minimum characters for all words
def minimumCharactersForWords(words):
    if words is None or len(words) == 0:
        return []

    map = {}

    for word in words:
        characters = {}
        for c in word:
            lst = characters.get(c, [])
            lst.append(c)
            characters[c] = lst

        for c, l in characters.items():
            if c in map:
                map[c] = max(map[c], characters[c], key=lambda x: len(x))
            else:
                map[c] = characters[c]


    res = []
    for l in map.values():
        res.extend(l)

    return res


if __name__ == '__main__':
    input = ["this", "that", "did", "deed", "them!", "a"]
    expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
    actual = minimumCharactersForWords(input)
    print(actual)
    assert actual == expected
