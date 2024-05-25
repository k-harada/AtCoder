MOD = 998244353


def solve(n, m):
    # 0番目の人を0で固定
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 1
    for i in range(n - 1):
        dp[i + 1][0] = dp[i][1]
        dp[i + 1][1] = (dp[i][0] * (m - 1) + dp[i][1] * (m - 2)) % MOD
    # print(dp)
    return (m * dp[-1][1]) % MOD


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(3, 3) == 6
    assert solve(4, 2) == 2
    # assert solve(987654, 456789) == 778634319


if __name__ == "__main__":
    test()
    main()
