from heapq import heappop, heappush


def solve(nn, mm, ss, line_list, cd_list):
    if ss > 5000:
        ss = 5000
    g = dict()
    for i in range(1, nn + 1):
        for s in range(5001):
            g[i * 10000 + s] = dict()
            if s + cd_list[i - 1][0] < 5000:
                g[i * 10000 + s][i * 10000 + s + cd_list[i - 1][0]] = cd_list[i - 1][1]
            elif s < 5000:
                g[i * 10000 + s][i * 10000 + 5000] = cd_list[i - 1][1]
    for u, v, a, b in line_list:
        for s in range(a, 5001):
            g[u * 10000 + s][v * 10000 + s - a] = b
            g[v * 10000 + s][u * 10000 + s - a] = b

    # start from 1
    # d[i, j] = best time at city i with silver j
    d = [10 ** 18] * ((nn + 1) * 10000)
    d[10000 + ss] = 0
    h = []
    heappush(h, (0, 10000 + ss))
    while len(h) > 0:
        t, u = heappop(h)
        for v in g[u].keys():
            if t + g[u][v] < d[v]:
                d[v] = t + g[u][v]
                heappush(h, (t + g[u][v], v))

    res = []
    for i in range(2, nn + 1):
        res.append(min(d[i * 10000:(i + 1) * 10000]))
    # print(res)
    return res


def main():
    n, m, s = map(int, input().split())
    line_list = [list(map(int, input().split())) for _ in range(m)]
    cd_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, s, line_list, cd_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 2, 1, [[1, 2, 1, 2], [1, 3, 2, 4]], [[1, 11], [1, 2], [2, 5]]) == [2, 14]
    assert solve(
        4, 4, 1, [[1, 2, 1, 5], [1, 3, 4, 4], [2, 4, 2, 2], [3, 4, 1, 1]], [[3, 1], [3, 1], [5, 2], [6, 4]]
    ) == [5, 5, 7]


if __name__ == "__main__":
    test()
    main()
