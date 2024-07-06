MOD = 998244353


def solve(n, k):
    no_touch = (((n * n - 2 * (n - 1)) % MOD) * pow(n * n, MOD - 2, MOD)) % MOD
    touch = (1 - no_touch) % MOD
    re_one = (2 * pow(n * n, MOD - 2, MOD)) % MOD
    stay = (1 - re_one) % MOD
    dp = [[0, 0] for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(k):
        dp[i + 1][0] = (dp[i][0] * no_touch + dp[i][1] * re_one) % MOD
        dp[i + 1][1] = (dp[i][0] * touch + dp[i][1] * stay) % MOD
    res = 1 * dp[-1][0] + (n + 2) * dp[-1][1] * pow(2, MOD - 2, MOD)
    res %= MOD

    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(2, 1) == 499122178
    assert solve(3, 2) == 554580198
    assert solve(4, 4) == 592707587


if __name__ == "__main__":
    test()
    main()
