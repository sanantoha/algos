from strings.one_edit import oneEdit


def test_oneEdit():
    stringOne = "hello"
    stringTwo = "helo"
    expected = True
    actual = oneEdit(stringOne, stringTwo)
    print(actual)
    assert actual == expected