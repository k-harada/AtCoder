def solve(n, x, y):
    dp = [[0] * 2 for _ in range(n)]
    dp[-1][0] = 1
    for i in range(n - 1, 0, -1):
        # Red
        dp[i][1] += x * dp[i][0]
        dp[i - 1][0] += dp[i][0]
        dp[i][0] = 0
        # Blue
        dp[i - 1][0] += dp[i][1]
        dp[i - 1][1] += y * dp[i][1]
        dp[i][1] = 0
    # print(dp)
    return dp[0][1]


def main():
    n, x, y = map(int, input().split())
    res = solve(n, x, y)
    print(res)


def test():
    assert solve(2, 3, 4) == 12
    assert solve(1, 5, 5) == 0
    assert solve(10, 5, 5) == 3942349900


if __name__ == "__main__":
    test()
    main()
