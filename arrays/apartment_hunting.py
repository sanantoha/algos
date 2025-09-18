
# O(b * r) time | O(b * r) space
def apartmentHunting(blocks, reqs):
    if blocks is None or reqs is None or len(blocks) == 0 or len(reqs) == 0:
        return -1

    distance = [{reg: float('inf') for reg in reqs} for _ in range(len(blocks))]

    for (k, v) in blocks[0].items():
        if v:
            distance[0][k] = 0

    for i in range(1, len(blocks)):
        for req in reqs:
            if blocks[i][req]:
                distance[i][req] = 0
            else:
                distance[i][req] = min(distance[i - 1][req] + 1, distance[i][req])

    for i in reversed(range(len(blocks) - 1)):
        for req in reqs:
            distance[i][req] = min(distance[i + 1][req] + 1, distance[i][req])

    min_dist = float('inf')
    min_dist_idx = 0
    for idx, dist in enumerate(distance):
        max_val = 0
        for req in reqs:
            max_val = max(max_val, dist[req])

        if max_val < min_dist:
            min_dist = max_val
            min_dist_idx = idx

    return min_dist_idx


if __name__ == '__main__':
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True},
    ]
    reqs = ["gym", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 3
