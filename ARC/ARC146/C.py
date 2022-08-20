MOD = 998244353


def solve(n):
    dp = [0] * (n + 2)
    dp[0] = 1
    dp[1] = pow(2, n, MOD)
    for i in range(1, n + 1):
        dp[i + 1] = dp[i] * (pow(2, n, MOD) - pow(2, i - 1, MOD))
        dp[i + 1] %= MOD
        dp[i + 1] *= pow(i + 1, MOD - 2, MOD)
        dp[i + 1] %= MOD
    # print(dp)

    return sum(dp) % MOD


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 15
    assert solve(146) == 743874490


if __name__ == "__main__":
    test()
    main()
