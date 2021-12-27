
# O(n ^ 2) time | O(n) space
def minNumberOfJumps(array):
    if array is None or len(array) == 0:
        return -1

    minJumps = [float('inf')] * len(array)
    minJumps[0] = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i and minJumps[i] > minJumps[j] + 1:
                minJumps[i] = minJumps[j] + 1


    return minJumps[-1]


# O(n) time | O(1) space
def minNumberOfJumps1(array):
    if array is None or len(array) == 0:
        return -1
    if len(array) == 1:
        return 0


    maxReach = array[0]
    steps = array[0]
    jumps = 0

    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = maxReach - i

    return jumps + 1


if __name__ == '__main__':
    actual = minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
    print(actual)
    assert actual == 4

    actual = minNumberOfJumps1([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
    print(actual)
    assert actual == 4
