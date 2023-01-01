
# O(n * w) time | O(n * w) space - where n is number of words and w is the length of longest word
def semordnilap(words):
    wordsSet = set(words)
    res = []

    for word in words:
        reverse = ''.join(reversed(word))
        if reverse in wordsSet and reverse != word:
            res.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return res


if __name__ == '__main__':
    input = ["desserts", "stressed", "hello"]
    expected = [["desserts", "stressed"]]
    actual = semordnilap(input)
    print(actual) # [['desserts', 'stressed']]