from heapq import heappop, heappush


def solve(n, m, h_list, uv_list):
    g = [[] for _ in range(n)]
    for u, v in uv_list:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    # ダイクストラ
    # 登りは距離0, 下りは標高差
    distance_list = [10 ** 18 + 7] * n
    distance_list[0] = 0
    h = []
    heappush(h, (0, 0))
    while len(h) > 0:
        u, d = heappop(h)
        if distance_list[u] < d:
            continue
        for v in g[u]:
            if h_list[u] >= h_list[v]:
                new_d = d
            else:
                new_d = d + h_list[v] - h_list[u]
            if new_d < distance_list[v]:
                distance_list[v] = new_d
                heappush(h, (v, new_d))

    res = 0
    for i in range(n):
        r = h_list[0] - h_list[i] - distance_list[i]
        res = max(res, r)
    return res


def main():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, h_list, uv_list)
    print(res)


def test():
    assert solve(4, 4, [10, 8, 12, 5], [(1, 2), (1, 3), (2, 3), (3, 4)]) == 3
    assert solve(2, 1, [0, 10], [(1, 2)]) == 0


if __name__ == "__main__":
    test()
    main()
