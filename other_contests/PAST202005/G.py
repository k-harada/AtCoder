import numpy as np
from collections import deque


def gold(x, y):
    res_temp_list = [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]
    res_list = []
    for s, t in res_temp_list:
        if 0 <= s <= 402 and 0 <= t <= 402:
            res_list.append((s, t))
    return res_list


def solve(n, xx, yy, xy_list):
    distance = 300000 * np.ones((403, 403), dtype=int)
    blocks = np.zeros((403, 403), dtype=int)
    distance[201, 201] = 0
    for x, y in xy_list:
        blocks[x + 201, y + 201] = 1

    queue = deque([(201, 201)])
    while len(queue) > 0:
        x, y = queue.popleft()
        # run
        for s, t in gold(x, y):
            if (s, t) == (xx + 201, yy + 201):
                return distance[x, y] + 1
            if blocks[s, t] == 0 and distance[s, t] > distance[x, y] + 1:
                distance[s, t] = distance[x, y] + 1
                queue.append((s, t))

    return -1


def main():
    n, x, y = map(int, input().split())
    xy_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, x, y, xy_list)
    print(res)


def test():
    assert solve(1, 2, 2, [[1, 1]]) == 3
    assert solve(1, 2, 2, [[2, 1]]) == 2
    assert solve(5, -2, 3, [[1, 1], [-1, 1], [0, 1], [-2, 1], [-3, 1]]) == 6


if __name__ == "__main__":
    test()
    main()
