MOD = 998244353


def solve(n, m):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[i][1] = 1
    for j in range(2, n + 1):
        for i in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * max(j - (i - 1) // m, 0)
            dp[i][j] %= MOD
    res_list = [dp[n][k] for k in range(1, n + 1)]
    # print(dp)
    # print(res_list)
    return res_list


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    for r in res:
        print(r)


def test():
    assert solve(4, 2) == [0, 2, 4, 1]
    assert solve(6, 6) == [1, 31, 90, 65, 15, 1]


if __name__ == "__main__":
    test()
    main()
