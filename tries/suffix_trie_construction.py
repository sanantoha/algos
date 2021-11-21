
# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n ^ 2) time | O(n ^ 2) space
    def populateSuffixTrieFrom(self, string):
        if string is None or len(string) == 0:
            self.root = {}
            return

        for i in range(len(string)):
            self.insertSubStringStartAt(i, string)


    def insertSubStringStartAt(self, start, string):
        curr = self.root
        for i in range(start, len(string)):
            letter = string[i]
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]

        curr[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        curr = self.root

        for letter in string:
            if letter not in curr:
                return False
            curr = curr[letter]

        return self.endSymbol in curr


if __name__ == '__main__':
    trie = SuffixTrie("babc")
    expected = {
        "c": {"*": True},
        "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
        "a": {"b": {"c": {"*": True}}},
    }
    assert trie.root == expected
    assert trie.contains("abc")