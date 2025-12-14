import pytest

from tries.suffix_trie_construction import SuffixTrie

@pytest.fixture(scope="class")
def trie():
    return SuffixTrie("babc")


class TestSuffixTrie:

    def test_contains(self):
        trie = SuffixTrie("babcd")

        assert trie.contains("bcd")


    def test_populateSuffixTrieFrom(self, trie):
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        assert trie.root == expected

