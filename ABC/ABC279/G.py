MOD = 998244353


def solve(n, k, c):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1
    dp[1][1] = c % MOD
    for i in range(1, n + 1):
        dp[i][1] = (dp[i - 1][1] + c * dp[i - 1][0]) % MOD
        dp[i][2] = dp[i - 1][2] * 2 % MOD  # 今の色で塗る or 前の色で塗る
        dp[i][2] += dp[i - 1][1] * (c - 1) % MOD  # 新しい色で塗る
        if i - k + 1 > 0:
            dp[i][2] += dp[i - k + 1][2] * (c - 2)
        dp[i][2] %= MOD
    # print(dp)
    res = (dp[n][1] + dp[n][2]) % MOD
    # print(res)
    return res


def main():
    n, k, c = map(int, input().split())
    res = solve(n, k, c)
    print(res)


def test():
    assert solve(3, 3, 3) == 21
    assert solve(10, 5, 2) == 1024
    assert solve(998, 244, 353) == 952364159


if __name__ == "__main__":
    test()
    main()
