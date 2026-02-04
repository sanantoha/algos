
# O(w * n * log(n)) time | O(w * n) space - w number of words and n is the length of the longest word
def groupAnagrams(words):
    wordsMap = {}

    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in wordsMap:
            wordsMap[sortedWord].append(word)
        else:
            wordsMap[sortedWord] = [word]

    return list(wordsMap.values())


def compare(expected, output):
    if len(expected) == 0:
        assert output == expected
        return
    assert len(expected) == len(output)
    for group in expected:
        assert sorted(group) in output


if __name__ == '__main__':
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
    output = list(map(lambda x: sorted(x), groupAnagrams(words)))
    expected = list(map(lambda x: sorted(x), expected))

    print(output)
    print(expected)
    compare(expected, output)
