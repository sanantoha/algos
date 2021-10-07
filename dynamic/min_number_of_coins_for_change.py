
# O(n * d) time | O(n) space
def min_number_of_coins_for_change(n, denoms):

    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0

    for denom in denoms:
        for amount in range(1, n + 1):
            if amount >= denom:
                dp[amount] = min(dp[amount - denom] + 1, dp[amount])

    return dp[n] if dp[n] != float('inf') else -1


if __name__ == '__main__':
    print(min_number_of_coins_for_change(7, [1, 5, 10]))
    assert min_number_of_coins_for_change(7, [1, 5, 10]) == 3