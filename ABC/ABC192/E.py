from collections import deque


def solve(n, m, x, y, abtk_list):
    g = [[] for _ in range(n + 1)]
    for a, b, t, k in abtk_list:
        g[a].append((b, t, k))
        g[b].append((a, t, k))
    reach_time = [10 ** 19 + 7] * (n + 1)
    reach_time[x] = 0

    queue = deque([x])
    while len(queue):
        p = queue.popleft()
        for q, t, k in g[p]:
            arr = k * ((reach_time[p] - 1) // k + 1) + t
            if arr < reach_time[q]:
                reach_time[q] = arr
                queue.append(q)

    if reach_time[y] < 10 ** 19 + 7:
        return reach_time[y]
    else:
        return -1


def main():
    n, m, x, y = map(int, input().split())
    abtk_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, x, y, abtk_list)
    print(res)


def test():
    assert solve(3, 2, 1, 3, [(1, 2, 2, 3), (2, 3, 3, 4)]) == 7
    assert solve(3, 2, 3, 1, [(1, 2, 2, 3), (2, 3, 3, 4)]) == 5
    assert solve(3, 0, 3, 1, []) == -1


if __name__ == "__main__":
    test()
    main()
