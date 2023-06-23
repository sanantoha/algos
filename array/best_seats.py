
# O(n) time | O(1) space
def bestSeat(seats):

    bestSeatIdx = -1
    left = 0
    maxSpace = 0

    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1

        availableSeats = right - left - 1
        if availableSeats > maxSpace:
            maxSpace = availableSeats
            bestSeatIdx = (left + right) // 2
        left = right

    return bestSeatIdx


if __name__ == '__main__':
    actual = bestSeat([1, 0, 1, 0, 0, 0, 1])
    assert actual == 4

    actual = bestSeat([1])
    assert actual == -1

    actual = bestSeat([1, 0, 1])
    assert actual == 1

    actual = bestSeat([1, 0, 0, 1])
    assert actual == 1

    actual = bestSeat([1, 1, 1])
    assert actual == -1

    actual = bestSeat([1, 0, 0, 1, 0, 0, 1])
    assert actual == 1

    actual = bestSeat([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    assert actual == 3
