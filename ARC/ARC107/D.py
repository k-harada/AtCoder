MOD = 998244353


def solve(n, k):

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if 2 * j <= i:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % MOD
            else:
                dp[i][j] = dp[i - 1][j - 1]
    # print(dp)
    return dp[n][k]


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(4, 2) == 2
    assert solve(2525, 425) == 687232272


if __name__ == "__main__":
    test()
    main()
