from heapq import heappush, heappop


def solve(n, m, abc_list):
    loop = [10 ** 9 + 7] * (n + 1)
    g = dict()
    for i in range(1, n + 1):
        g[i] = dict()
    for a, b, c in abc_list:
        if a == b:
            loop[a] = min(loop[a], c)
        else:
            if b in g[a].keys():
                g[a][b] = min(g[a][b], c)
            else:
                g[a][b] = c
    res_list = [-1] * n
    for i in range(1, n + 1):
        h = [(0, i)]
        d_list = [10 ** 9 + 7] * (n + 1)
        while len(h):
            d_temp, p = heappop(h)
            # print(d_temp, p)
            if d_list[p] < 10 ** 9 + 7:
                continue
            if d_temp > 0:
                d_list[p] = d_temp
            if p == i and d_list[i] < 10 ** 9 + 7:
                break
            for q in g[p].keys():
                if d_temp > d_list[q]:
                    continue
                if d_list[q] > d_temp + g[p][q]:
                    heappush(h, (d_temp + g[p][q], q))
                else:
                    continue
        d = min(d_list[i], loop[i])
        # print(d_list)
        if d < 10 ** 9 + 7:
            res_list[i - 1] = d
    # print(res_list)
    return res_list


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res_list = solve(n, m, abc_list)
    for res in res_list:
        print(res)


def test():
    assert solve(4, 4, [(1, 2, 5), (2, 3, 10), (3, 1, 15), (4, 3, 20)]) == [30, 30, 30, -1]
    assert solve(4, 6, [(1, 2, 5), (1, 3, 10), (2, 4, 5), (3, 4, 10), (4, 1, 10), (1, 1, 10)]) == [10, 20, 30, 20]
    assert solve(4, 7, [(1, 2, 10), (2, 3, 30), (1, 4, 15), (3, 4, 25), (3, 4, 20), (4, 3, 20), (4, 3, 30)]) == [-1, -1, 40, 40]


if __name__ == "__main__":
    test()
    main()
