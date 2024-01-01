
# O(n ^ 2) time | O(n) space
def minRewards(scores):
    if scores is None or len(scores) == 0:
        return 0

    rewards = [1] * len(scores)

    for i in range(1, len(scores)):
        j = i - 1
        if scores[j] < scores[i]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)


# O(n) time | O(n) space
def minRewards1(scores):
    if scores is None or len(scores) == 0:
        return 0

    rewards = [1] * len(scores)

    lowerIdxs = getLowerIdxs(scores)

    for idx in lowerIdxs:
        expandLowerIdxs(scores, rewards, idx)

    return sum(rewards)


def getLowerIdxs(scores):
    idxs = []
    if len(scores) == 1:
        idxs.append(0)
        return idxs

    for i in range(len(scores)):
        if i == 0 and scores[i] < scores[i + 1]:
            idxs.append(i)
        if i == len(scores) - 1 and scores[i] < scores[i - 1]:
            idxs.append(i)
        if i == 0 or i == len(scores) - 1:
            continue
        if scores[i] < scores[i + 1] and scores[i] < scores[i - 1]:
            idxs.append(i)

    return idxs


def expandLowerIdxs(scores, rewards, idx):
    lidx = idx - 1
    while lidx >= 0 and scores[lidx] > scores[lidx + 1]:
        rewards[lidx] = max(rewards[lidx], rewards[lidx + 1] + 1)
        lidx -= 1

    ridx = idx + 1
    while ridx < len(scores) and scores[ridx - 1] < scores[ridx]:
        rewards[ridx] = rewards[ridx - 1] + 1
        ridx += 1


# O(n) time | O(n) space
def minRewards2(scores):
    if scores is None or len(scores) == 0:
        return 0

    rewards = [1] * len(scores)

    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)


if __name__ == '__main__':
    actual = minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])
    print(actual)
    assert actual == 25

    actual = minRewards1([8, 4, 2, 1, 3, 6, 7, 9, 5])
    print(actual)
    assert actual == 25

    actual = minRewards2([8, 4, 2, 1, 3, 6, 7, 9, 5])
    print(actual)
    assert actual == 25
