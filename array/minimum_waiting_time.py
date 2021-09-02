# O(n * log(n)) time | O(1) space
def minimum_waiting_time(queries):
    queries.sort()

    total_sums = 0
    prev = 0

    for duration in queries:
        total_sums += prev
        prev += duration

    return total_sums


# O(n * log(n)) time | O(1) space
def minimum_waiting_time1(queries):
    queries.sort()

    total_sums = 0

    for idx, duration in enumerate(queries):
        query_idx = len(queries) - (idx + 1)
        total_sums += duration * query_idx

    return total_sums


if __name__ == '__main__':
    print(minimum_waiting_time([3, 2, 1, 2, 6]))
    print(minimum_waiting_time1([3, 2, 1, 2, 6]))
