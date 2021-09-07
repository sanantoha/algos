
# O(n * log(n)) time | O(1) space
def tandem_bicycle(red_shirt_speed, blue_shirt_speed, fastest):
    red_shirt_speed.sort()
    blue_shirt_speed.sort(reverse=fastest)

    total_speed = 0
    for idx in range(len(red_shirt_speed)):
        red = red_shirt_speed[idx]
        blue = blue_shirt_speed[idx]
        total_speed += max(red, blue)

    return total_speed


if __name__ == '__main__':
    print(
        tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True)
    )
