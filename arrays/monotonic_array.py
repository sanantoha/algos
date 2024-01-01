
# O(n) time | O(1) space
def monotonic_array(array):
    if array is None or len(array) <= 2:
        return True

    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        if break_direction(direction, array[i - 1], array[i]):
            return False

    return True


def break_direction(direction, prev, curr):
    diff = curr - prev
    if direction > 0:
        return diff < 0
    return diff > 0


if __name__ == '__main__':
    print(monotonic_array([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
