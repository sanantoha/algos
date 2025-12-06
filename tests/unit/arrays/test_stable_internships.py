from arrays.stable_internships import stableInternships


def test_stable_internships():
    interns = [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
    teams = [[2, 1, 0], [0, 1, 2], [0, 1, 2]]
    expected = [[0, 1], [1, 0], [2, 2]]
    actual = stableInternships(interns, teams)
    print(actual)
    assert len(actual) == len(expected)

    for match in expected:
        containsMatch = False
        for actualMatch in actual:
            if actualMatch[0] == match[0] and actualMatch[1] == match[1]:
                containsMatch = True
        assert containsMatch