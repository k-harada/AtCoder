from heapq import heappop, heappush


def solve(n_1, n_2, m, ab_list):
    g = [[] for _ in range(n_1 + n_2 + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)
    d_list = [n_1 + n_2] * (n_1 + n_2 + 1)
    h = []
    heappush(h, (0, 1))
    while len(h):
        d, p = heappop(h)
        if d_list[p] <= d:
            continue
        d_list[p] = d
        for q in g[p]:
            if d_list[q] > d + 1:
                heappush(h, (d + 1, q))
    h = []
    heappush(h, (0, n_1 + n_2))
    while len(h):
        d, p = heappop(h)
        if d_list[p] <= d:
            continue
        d_list[p] = d
        for q in g[p]:
            if d_list[q] > d + 1:
                heappush(h, (d + 1, q))
    # print(d_list)
    res = max(d_list[1:n_1 + 1]) + max(d_list[n_1 + 1:]) + 1
    return res


def main():
    n_1, n_2, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n_1, n_2, m, ab_list)
    print(res)


def test():
    assert solve(3, 4, 6, [(1, 2), (2, 3), (4, 5), (4, 6), (1, 3), (6, 7)]) == 5


if __name__ == "__main__":
    test()
    main()
