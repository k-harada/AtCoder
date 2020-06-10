MOD = 10 ** 9 + 7


def solve(n, m):
    # factorial
    fac = [0] * (n + 1)
    fac_inv = [0] * (n + 1)
    fac[0] = 1
    for i in range(n):
        fac[i + 1] = (fac[i] * (i + 1)) % MOD
    fac_inv[-1] = pow(fac[-1], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        fac_inv[i] = (fac_inv[i + 1] * (i + 1)) % MOD
    # dp
    dp = [[0] * (n + 1) for _ in range(m)]
    for i in range(n + 1):
        dp[0][i] = (fac[n] * fac_inv[i] * fac_inv[n - i]) % MOD

    for i in range(m - 1):
        for j in range(n + 1):
            # equal
            dp[i + 1][j] += dp[i][j]
            # add 1
            if j < n:
                dp[i + 1][j + 1] += dp[i][j] * (n - j)
            # delete 1
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j] * j
        for j in range(n):
            dp[i + 1][j] %= MOD
    print(dp)
    return sum(dp[-1]) % MOD


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(2, 5) == 352


if __name__ == "__main__":
    test()
    main()
