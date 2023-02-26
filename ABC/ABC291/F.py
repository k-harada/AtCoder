from heapq import heappush, heappop


def solve(n, m, s_list):
    d1_list = [-1] * (n + 1)
    h1 = []
    heappush(h1, (0, 1))
    while len(h1):
        d1, p = heappop(h1)
        if d1_list[p] >= 0:
            continue
        d1_list[p] = d1
        for i in range(m):
            if s_list[p - 1][i] == "1":
                q = p + i + 1
                heappush(h1, (d1 + 1, q))
    # reverse
    reverse_g = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s_list[i][j] == "1":
                reverse_g[i + j + 2].append(i + 1)

    dn_list = [-1] * (n + 1)
    hn = []
    heappush(hn, (0, n))
    while len(hn):
        dn, p = heappop(hn)
        if dn_list[p] >= 0:
            continue
        dn_list[p] = dn
        for q in reverse_g[p]:
            heappush(hn, (dn + 1, q))
    res_list = [n + 1] * (n + 1)
    for k in range(2, n):
        for i in range(max(1, k - m + 1), k):
            d1 = d1_list[i]
            for j in range(m):
                if s_list[i - 1][j] == "1" and i + j + 1 > k:
                    dn = dn_list[i + j + 1]
                    d = d1 + dn + 1
                    if d1 >= 0 and dn >= 0:
                        res_list[k] = min(res_list[k], d)
    for i in range(2, n):
        if res_list[i] == n + 1:
            res_list[i] = -1
    res = " ".join([str(a) for a in res_list[2:n]])
    # print(d1_list)
    # print(dn_list)
    # print(res_list)
    return res


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(n)]
    res = solve(n, m, s_list)
    print(res)


def test():
    assert solve(5, 2, ["11", "01", "11", "10", "00"]) == "2 3 2"
    assert solve(6, 3, ["101", "001", "101", "000", "100", "000"]) == "-1 3 3 -1"


if __name__ == "__main__":
    test()
    main()
