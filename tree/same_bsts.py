
# O(n ^ 2) time | O(n ^ 2) space
def sameBsts(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        return True
    if not arrayOne or not arrayTwo or arrayOne[0] != arrayTwo[0]:
        return False

    lOne, rOne = partition(arrayOne)
    lTwo, rTwo = partition(arrayTwo)

    return sameBsts(lOne, lTwo) and sameBsts(rOne, rTwo)


def partition(array):
    l, r = [], []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            l.append(array[i])
        else:
            r.append(array[i])

    return l, r


# O(n ^ 2) time | O(n) space
def sameBsts1(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        return True
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def areSameBsts(arrayOne, arrayTwo, idxOne, idxTwo, minVal, maxVal):
    if idxOne == -1 or idxTwo == -1:
        return idxOne == idxTwo
    if arrayOne[idxOne] != arrayTwo[idxTwo]:
        return False

    leftIdxOne = getIdxOfFirstSmaller(arrayOne, idxOne, minVal)
    leftIdxTwo = getIdxOfFirstSmaller(arrayTwo, idxTwo, minVal)
    rightIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, idxOne, maxVal)
    rightIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, idxTwo, maxVal)

    currVal = arrayOne[idxOne]
    return areSameBsts(arrayOne, arrayTwo, leftIdxOne, leftIdxTwo, minVal, currVal) and \
            areSameBsts(arrayOne, arrayTwo, rightIdxOne, rightIdxTwo, currVal, maxVal)


def getIdxOfFirstSmaller(array, idx, minVal):
    for i in range(idx + 1, len(array)):
        if array[idx] > array[i] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstBiggerOrEqual(array, idx, maxVal):
    for i in range(idx + 1, len(array)):
        if array[idx] <= array[i] and array[i] < maxVal:
            return i
    return -1


if __name__ == '__main__':
    arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    assert sameBsts(arrayOne, arrayTwo)

    assert sameBsts1(arrayOne, arrayTwo)

