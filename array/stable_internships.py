
# O(n ^ 2) time | O(n ^ 2) space
def stableInternships(interns, teams):
    chosenIntern = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)
    teamMaps = []

    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)

    while freeInterns:
        internNum = freeInterns.pop()

        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if teamPreference not in chosenIntern:
            chosenIntern[teamPreference] = internNum
            continue

        previousIntern = chosenIntern[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNum]

        if currentInternRank < previousInternRank:
            chosenIntern[teamPreference] = internNum
            freeInterns.append(previousIntern)
        else:
            freeInterns.append(internNum)

    matches = [[internNum, teamNum] for teamNum, internNum in chosenIntern.items()]
    return matches


if __name__ == '__main__':
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