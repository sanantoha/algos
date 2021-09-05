
# O(n * log(n)) time | O(1) space
def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()

    is_red_higher = red_shirt_heights[0] > blue_shirt_heights[0]

    for idx in range(len(red_shirt_heights)):
        if is_red_higher and red_shirt_heights[idx] <= blue_shirt_heights[idx]:
            return False
        if not is_red_higher and red_shirt_heights[idx] >= blue_shirt_heights[idx]:
            return False

    return True


if __name__ == '__main__':
    print(class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
