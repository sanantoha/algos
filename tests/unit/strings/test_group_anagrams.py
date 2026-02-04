from strings.group_anagrams import compare, groupAnagrams


def test_groupAnagrams():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
    output = list(map(lambda x: sorted(x), groupAnagrams(words)))
    expected = list(map(lambda x: sorted(x), expected))

    print(output)
    print(expected)
    compare(expected, output)