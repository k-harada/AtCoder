from heapq import heappop, heappush


def solve(n, m, uvw_list, k, a_list, d, x_list):
    g = [[] for _ in range(n)]
    for u, v, w in uvw_list:
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    res = [d + 1] * n
    edge_list = []
    oneday_edge_list = []
    for a in a_list:
        res[a - 1] = 0
        for v, w in g[a - 1]:
            heappush(edge_list, (w, v))

    for da in range(1, d + 1):
        new_list = []
        # 通常感染
        while len(edge_list):
            w, v = heappop(edge_list)
            if w > x_list[da - 1]:
                heappush(edge_list, (w, v))
                break
            if res[v] > da:
                heappush(oneday_edge_list, (w, v))

        # 当日貫通感染
        while len(oneday_edge_list):
            distance, u = heappop(oneday_edge_list)
            if res[u] <= da:
                continue
            res[u] = da
            new_list.append(u)
            for v, w in g[u]:
                if distance + w <= x_list[da - 1]:
                    if res[v] > da:
                        heappush(oneday_edge_list, (distance + w, v))

        # 新規edge追加
        while len(new_list):
            u = new_list.pop()
            for v, w in g[u]:
                if res[v] == d + 1:
                    heappush(edge_list, (w, v))

    for i in range(n):
        if res[i] == d + 1:
            res[i] = -1

    return res


def main():
    n, m = map(int, input().split())
    uvw_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    a_list = list(map(int, input().split()))
    d = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, m, uvw_list, k, a_list, d, x_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 4, [
        (1, 2, 2), (2, 3, 1), (2, 4, 3), (3, 4, 2)
    ], 1, [1], 2, [3, 3]) == [0, 1, 1, 2]
    assert solve(7, 7, [
        (1, 2, 2), (2, 3, 3), (3, 4, 1), (4, 5, 1), (5, 6, 3),
        (3, 7, 1), (4, 7, 1)
    ], 2, [1, 6], 2, [2, 3]) == [0, 1, 2, -1, 2, 0, -1]
    assert solve(5, 1, [(1, 2, 5)], 2, [1, 3], 3, [3, 7, 5]) == [0, 2, 0, -1, -1]


if __name__ == "__main__":
    test()
    main()
