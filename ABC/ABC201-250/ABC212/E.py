LARGE = 998244353


def solve(n, m, k, uv_list):
    g = [[] for _ in range(n)]
    for u, v in uv_list:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    dp = [[0] * n for _ in range(k + 1)]
    dp[0][0] = 1
    for d in range(k):
        sum_d = sum(dp[d]) % LARGE
        for p in range(n):
            dp[d + 1][p] = sum_d - dp[d][p]
            for q in g[p]:
                dp[d + 1][p] -= dp[d][q]
            dp[d + 1][p] %= LARGE
    return dp[-1][0]


def main():
    n, m, k = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, k, uv_list)
    print(res)


def test():
    assert solve(3, 1, 4, [(2, 3)]) == 4
    assert solve(3, 3, 3, [(1, 2), (1, 3), (2, 3)]) == 0
    assert solve(5, 3, 100, [(1, 2), (4, 5), (2, 3)]) == 428417047


if __name__ == "__main__":
    test()
    main()
