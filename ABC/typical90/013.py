from heapq import heappush, heappop


def solve(n, m, abc_list):
    g = [[] for _ in range(n + 1)]
    for a, b, c in abc_list:
        g[a].append((b, c))
        g[b].append((a, c))

    # dist from 1
    dist_1 = [n * 10000 + 1] * (n + 1)
    h = []
    heappush(h, (0, 1))
    while len(h):
        d, p = heappop(h)
        if d < dist_1[p]:
            dist_1[p] = d
            for q, c in g[p]:
                heappush(h, (d + c, q))

    # dist from n
    dist_n = [n * 10000 + 1] * (n + 1)
    h = []
    heappush(h, (0, n))
    while len(h):
        d, p = heappop(h)
        if d < dist_n[p]:
            dist_n[p] = d
            for q, c in g[p]:
                heappush(h, (d + c, q))
    res = []
    for i in range(1, n + 1):
        res.append(dist_1[i] + dist_n[i])
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, abc_list)
    for r in res:
        print(r)


def test():
    assert solve(7, 9, [
        (1, 2, 2), (1, 3, 3), (2, 5, 2), (3, 4, 1), (3, 5, 4), (4, 7, 5), (5, 6, 1), (5, 7, 6), (6, 7, 3)
    ]) == [8, 8, 9, 9, 8, 8, 8]
    assert solve(4, 3, [(1, 2, 1), (2, 3, 10), (3, 4, 100)]) == [111, 111, 111, 111]
    assert solve(4, 3, [(1, 2, 314), (1, 3, 159), (1, 4, 265)]) == [265, 893, 583, 265]


if __name__ == "__main__":
    test()
    main()
