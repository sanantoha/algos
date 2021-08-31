
# O(n * log(n)) time | O(1) space
def non_constructible_changes(coins):
    sorted_coins = sorted(coins)

    current_change_created = 0

    for coin in sorted_coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin

    return current_change_created + 1


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]
    print(non_constructible_changes(coins))
