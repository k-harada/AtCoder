MOD = 998244353


def solve(n, m, k):
    # dp
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(k):
        for j in range(n):
            for d in range(1, m + 1):
                if j + d <= n:
                    dp[i + 1][j + d] += dp[i][j]
                else:
                    dp[i + 1][n - ((j + d) - n)] += dp[i][j]
        for j in range(n + 1):
            dp[i + 1][j] %= MOD
    res = 0
    div = 1
    div_base = pow(m, MOD - 2, MOD)
    for i in range(k + 1):
        res += dp[i][n] * div
        res %= MOD
        div *= div_base
        div %= MOD
    return res


def main():
    n, m, k = map(int, input().split())
    res = solve(n, m, k)
    print(res)


def test():
    assert solve(2, 2, 1) == 499122177
    assert solve(10, 5, 6) == 184124175
    assert solve(100, 1, 99) == 0


def test_large():
    print(solve(1000, 10, 1000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
