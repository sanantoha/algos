
# O(2 ^ (w + h)) | O(w + h) space
def numbers_of_ways_to_traverse_graph_rec(width, height):
    if width == 1 or height == 1:
        return 1
    return numbers_of_ways_to_traverse_graph(width - 1, height) + numbers_of_ways_to_traverse_graph(width, height - 1)


# O(w * h) time | O(w * h) space
def numbers_of_ways_to_traverse_graph(width, height):
    dp = [[1 for _ in range(width)] for _ in range(height)]

    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


# O(w + h) time | O(1) time
def numbers_of_ways_to_traverse_graph_math(width, height):
    x_distance = width - 1
    y_distance = height - 1
    return factorial(x_distance + y_distance) // (factorial(x_distance) * factorial(y_distance))


def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    assert numbers_of_ways_to_traverse_graph_rec(4, 3) == 10
    assert numbers_of_ways_to_traverse_graph(4, 3) == 10
    assert numbers_of_ways_to_traverse_graph_math(4, 3) == 10
