from strings.semordinal import semordnilap


def test_semordnilap():
    input = ["desserts", "stressed", "hello"]
    expected = [["desserts", "stressed"]]
    actual = semordnilap(input)
    print(actual)  # [['desserts', 'stressed']]
    assert actual == expected