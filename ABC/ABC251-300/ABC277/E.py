from heapq import heappop, heappush


def solve(n, m, k, uva_list, s_list):
    dist = [10 * n] * (2 * n + 1)
    g = [[] for _ in range(2 * n + 1)]
    for u, v, a in uva_list:
        if a == 1:
            g[u].append(v)
            g[v].append(u)
        else:
            g[u + n].append(v + n)
            g[v + n].append(u + n)
    for s in s_list:
        g[s].append(s + n)
        g[s + n].append(s)

    h = []
    dist[1] = 0
    heappush(h, (0, 1))

    while len(h) > 0:
        d, p = heappop(h)
        for q in g[p]:
            if abs(p - q) == n:
                if dist[q] > d:
                    dist[q] = d
                    heappush(h, (d, q))
            else:
                if dist[q] > d + 1:
                    dist[q] = d + 1
                    heappush(h, (d + 1, q))
    res = min(dist[n], dist[2 * n])
    if res == 10 * n:
        res = -1
    return res


def main():
    n, m, k = map(int, input().split())
    uva_list = [tuple(map(int, input().split())) for _ in range(m)]
    s_list = list(map(int, input().split()))
    res = solve(n, m, k, uva_list, s_list)
    print(res)


def test():
    assert solve(5, 5, 2, [(1, 3, 0), (2, 3, 1), (5, 4, 1), (2, 1, 1), (1, 4, 0)], [3, 4]) == 5
    assert solve(4, 4, 2, [(4, 3, 0), (1, 2, 1), (1, 2, 0), (2, 2, 1)], [2, 4]) == -1


if __name__ == "__main__":
    test()
    main()
