from strings.common_characters import commonCharacters


def test_commonCharacters():
    input = ["abc", "bcdc", "badca"]
    expected = ["b", "c"]
    actual = commonCharacters(input)
    actual.sort()
    print(actual)
    assert actual == expected