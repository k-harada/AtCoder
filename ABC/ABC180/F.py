MOD = 10 ** 9 + 7


def solve(n, m, ll):

    if ll == 1:
        if m == 0:
            return 1
        else:
            return 0

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    fact_inv = [1] * (n + 1)
    fact_inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % MOD
    fact_2 = [1] * (n + 1)
    for i in range(n + 1):
        fact_2[i] = fact[i] * fact_inv[2] % MOD

    # pre-compute
    ncr_fact_21 = [[0] * ll for _ in range(n + 1)]
    ncr_fact_20 = [[0] * ll for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(ll, i + 1)):
            ncr_fact_21[i][j] = (((fact[i] * fact_inv[j]) % MOD) * ((fact_inv[i - j] * fact_2[j + 1]) % MOD)) % MOD
            ncr_fact_20[i][j] = (((fact[i] * fact_inv[j]) % MOD) * ((fact_inv[i - j] * fact_2[j]) % MOD)) % MOD

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # less-than ll
    for i in range(n):
        for j in range(m + 1):
            # single
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            # 2-loop
            if i + 2 <= n and j + 2 <= m and ll > 2:
                dp[i + 2][j + 2] += dp[i][j] * (n - i - 1)
                dp[i + 2][j + 2] %= MOD
            for k in range(2, min([n - i + 1, m - j + 2, ll])):
                # path
                dp[i + k][j + k - 1] += dp[i][j] * ncr_fact_21[n - i - 1][k - 1]
                dp[i + k][j + k - 1] %= MOD
            for k in range(3, min([n - i + 1, m - j + 1, ll])):
                # loop
                dp[i + k][j + k] += dp[i][j] * ncr_fact_20[n - i - 1][k - 1]
                dp[i + k][j + k] %= MOD

    res_1 = dp[n][m]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # less-than or equal ll
    for i in range(n):
        for j in range(m + 1):
            # single
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            # 2-loop
            if i + 2 <= n and j + 2 <= m:
                dp[i + 2][j + 2] += dp[i][j] * (n - i - 1)
                dp[i + 2][j + 2] %= MOD
            for k in range(2, min([n - i + 1, m - j + 2, ll + 1])):
                # path
                dp[i + k][j + k - 1] += dp[i][j] * ncr_fact_21[n - i - 1][k - 1]
                dp[i + k][j + k - 1] %= MOD
            for k in range(3, min([n - i + 1, m - j + 1, ll + 1])):
                # loop
                dp[i + k][j + k] += dp[i][j] * ncr_fact_20[n - i - 1][k - 1]
                dp[i + k][j + k] %= MOD

    res_2 = dp[n][m]

    return (res_2 - res_1) % MOD


def main():
    n, m, ll = map(int, input().split())
    res = solve(n, m, ll)
    print(res)


def test():
    assert solve(3, 2, 3) == 3
    assert solve(4, 3, 2) == 6
    assert solve(300, 290, 140) == 211917445


if __name__ == "__main__":
    test()
    main()
