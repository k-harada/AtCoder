MOD = 998244353


def solve(n, t):
    dp = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    res = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
    for i in range(2 * n):
        if t[i] != "-":
            for j in range(n):
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
                res[i + 1][j + 1] += res[i][j]
            for j in range(1, n + 1):
                dp[i + 1][-j + 1] += dp[i][-j]
                dp[i + 1][-j + 1] %= MOD
                res[i + 1][-j + 1] += res[i][-j] + dp[i][-j] * (2 * j - 1)
                res[i + 1][-j + 1] %= MOD
        if t[i] != "+":
            for j in range(1, n + 1):
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
                res[i + 1][j - 1] += res[i][j] + dp[i][j] * (2 * j - 1)
                res[i + 1][j - 1] %= MOD
            for j in range(n):
                dp[i + 1][-j - 1] += dp[i][-j]
                dp[i + 1][-j - 1] %= MOD
                res[i + 1][-j - 1] += res[i][-j]

        # print(dp)
        # print(res)
    # print(dp)
    # print(res)
    return res[-1][0]


def main():
    n = int(input())
    t = input()
    res = solve(n, t)
    print(res)


def test():
    assert solve(2, "++--") == 4
    assert solve(2, "+-+-") == 2
    assert solve(2, "+??-") == 6
    assert solve(17, "??????????????????????????????????") == 285212526


if __name__ == "__main__":
    test()
    main()
