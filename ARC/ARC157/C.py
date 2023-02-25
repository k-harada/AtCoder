MOD = 998244353


def solve(h, w, s_list):
    dp = [[[0, 0, 0] for _1 in range(w)] for _2 in range(h)]
    dp[0][0][2] = 1
    # ２乗和, 和, 個数
    for j in range(1, w):
        dp[0][j][2] = 1
        if s_list[0][j] == s_list[0][j - 1] == "Y":
            dp[0][j][1] = dp[0][j - 1][1] + 1
            dp[0][j][0] = (dp[0][j][1] ** 2) % MOD
        else:
            dp[0][j][1] = dp[0][j - 1][1]
            dp[0][j][0] = dp[0][j - 1][0]

    for i in range(1, h):
        dp[i][0][2] = 1
        if s_list[i][0] == s_list[i - 1][0] == "Y":
            dp[i][0][1] = dp[i - 1][0][1] + 1
            dp[i][0][0] = (dp[i][0][1] ** 2) % MOD
        else:
            dp[i][0][1] = dp[i - 1][0][1]
            dp[i][0][0] = dp[i - 1][0][0]
        for j in range(1, w):
            dp[i][j][2] = (dp[i - 1][j][2] + dp[i][j - 1][2]) % MOD
            if s_list[i][j] == s_list[i - 1][j] == "Y":
                dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
                dp[i][j][0] += (dp[i - 1][j][0] + 2 * dp[i - 1][j][1] + dp[i - 1][j][2]) % MOD
            else:
                dp[i][j][1] += dp[i - 1][j][1]
                dp[i][j][0] += dp[i - 1][j][0]
            if s_list[i][j] == s_list[i][j - 1] == "Y":
                dp[i][j][1] += dp[i][j - 1][1] + dp[i][j - 1][2]
                dp[i][j][0] += (dp[i][j - 1][0] + 2 * dp[i][j - 1][1] + dp[i][j - 1][2]) % MOD
            else:
                dp[i][j][1] += dp[i][j - 1][1]
                dp[i][j][0] += dp[i][j - 1][0]
            dp[i][j][0] %= MOD
            dp[i][j][1] %= MOD
    return dp[-1][-1][0]


def main():
    h, w = map(int, input().split())
    s_list = [input() for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(2, 2, ["YY", "XY"]) == 4
    assert solve(2, 2, ["XY", "YY"]) == 2
    assert solve(10, 20, [
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY",
        "YYYYYYYYYYYYYYYYYYYY"
    ]) == 423787835


if __name__ == "__main__":
    test()
    main()
