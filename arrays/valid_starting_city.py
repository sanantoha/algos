
# O(n ^ 2) time | O(1) time
def valid_starting_city(distances, fuel, mpg):
    len_of_cities = len(distances)

    for start_idx in range(len_of_cities):
        miles_remain = 0
        for city_idx in range(start_idx, start_idx + len_of_cities):
            idx = city_idx % len_of_cities
            miles_remain += fuel[idx] * mpg - distances[idx]
            if miles_remain < 0:
                break

        if miles_remain >= 0:
            return start_idx

    return -1


# O(n) time | O(1) space
def valid_starting_city1(distances, fuel, mpg):
    remain_distance = 0
    min_remain_distance = 0
    min_idx = 0

    for idx in range(1, len(fuel)):
        remain_distance += fuel[idx - 1] * mpg - distances[idx - 1]
        if remain_distance < min_remain_distance:
            min_remain_distance = remain_distance
            min_idx = idx

    return min_idx


if __name__ == '__main__':
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    expected = 4
    actual = valid_starting_city(distances, fuel, mpg)
    print(actual)
    assert actual == expected

    actual1 = valid_starting_city1(distances, fuel, mpg)
    print(actual1)
    assert actual1 == expected
