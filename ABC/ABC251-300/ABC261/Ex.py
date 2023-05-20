from collections import deque
from heapq import heappop, heappush


def solve(n, m, v, abc_list):
    g = [[] for _ in range(n + 1)]
    g_rev = [[] for _ in range(n + 1)]
    cnt_out = [0] * (n + 1)
    for a, b, c in abc_list:
        g[a].append((b, c))
        g_rev[b].append((a, c))
        cnt_out[a] += 1

    cnt_finite = [0] * n

    # 無限ループの検出
    queue = deque()
    dp_loop = [[True] * 2 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if cnt_out[i] == 0:
            dp_loop[i][0] = False
            dp_loop[i][1] = False
            queue.append((i, 0))
            queue.append((i, 1))
    while len(queue):
        q, k = queue.popleft()
        if k == 1:
            for p, c in g_rev[q]:
                dp_loop[p][0] = False
                queue.append((p, 0))
        else:
            for p, c in g_rev[q]:
                cnt_finite[p] += 1
                if cnt_finite[p] == cnt_out[p]:
                    dp_loop[p][1] = False
                    queue.append((p, 1))
    print(dp_loop)

    dp_value = [[10 ** 9, 0] for _ in range(n + 1)]
    h = []
    value_checked = [0] * (n + 1)
    for i in range(1, n + 1):
        if cnt_out[i] == 0:
            heappush(h, (0, i, 0))
            heappush(h, (0, i, 1))
    while len(h):
        x, q, t = heappop(h)
        print(x, q, t)
        if t == 0:
            dp_value[q][1] = x
            value_checked[q] += 1
            if value_checked[q] == cnt_out[q]:
                for p, c in g_rev[q]:
                    heappush(h, (dp_value[q][1] + c, p, 1))
        else:
            if dp_value[q][0] < 10 ** 9:
                continue
            dp_value[q][0] = x
            for p, c in g_rev[q]:
                heappush(h, (dp_value[q][0] + c, p, 0))

    print(dp_value)

    return 0


def main():
    n, m, v = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, v, abc_list)
    print(res)


def test():
    assert solve(7, 6, 1, [(1, 2, 1), (1, 3, 10), (2, 4, 100), (2, 5, 102), (3, 6, 20), (3, 7, 30)]) == 0
    assert solve(3, 6, 3, [(1, 2, 1), (2, 1, 2), (2, 3, 3), (3, 2, 4), (3, 1, 5), (1, 3, 6)]) == 0
    assert solve(4, 4, 1, [(1, 2, 1), (2, 3, 1), (3, 1, 1), (2, 4, 1)]) == 0


if __name__ == "__main__":
    test()
    main()
