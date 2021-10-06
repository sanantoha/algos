
# O(n * d) | O(n) time
def number_of_ways_to_make_change(n, denoms):
    if n < 0 or denoms is None or len(denoms) == 0:
        return 0

    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for coin in denoms:
        for amount in range(1, n + 1):
            if amount >= coin:
                dp[amount] += dp[amount - coin]

    return dp[n]


if __name__ == '__main__':
    print(number_of_ways_to_make_change(6, [1, 5]))
    assert number_of_ways_to_make_change(6, [1, 5]) == 2