
# O(n * log(n)) time | O(n) space
def merge_overlapping_intervals(intervals):
    if intervals is None or len(intervals) == 0:
        return [[]]

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    print(merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])) # [[1, 2], [3, 8], [9, 10]]
