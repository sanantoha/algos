
# O(t - s) time | O(t - s) space
def blackjackProbability(target, startingHand):
    memo = {}
    return round(helper(startingHand, target, memo), 3)

def helper(currentHand, target, memo):
    if currentHand in memo:
        return memo[currentHand]

    if currentHand > target:
        return 1
    if currentHand >= target - 4:
        return 0

    totalProbability = 0
    for drawCard in range(1, 11):
        totalProbability += 0.1 * helper(currentHand + drawCard, target, memo)

    memo[currentHand] = totalProbability
    return totalProbability


if __name__ == '__main__':
    actual = blackjackProbability(21, 15)
    print(actual)
    assert actual == 0.45

    actual = blackjackProbability(21, 21)
    print(actual)
    assert actual == 0

    actual = blackjackProbability(21, 20)
    print(actual)
    assert actual == 0

    actual = blackjackProbability(21, 17)
    print(actual)
    assert actual == 0

    actual = blackjackProbability(21, 12)
    print(actual)
    assert actual == 0.268

    actual = blackjackProbability(21, 5)
    print(actual)
    assert actual == 0.295

    actual = blackjackProbability(30, 25)
    print(actual)
    assert actual == 0.5