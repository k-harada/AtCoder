def solve(n, xy_list):
    dp = [[0] * 2 for _ in range(n + 1)]
    for i in range(n):
        x, y = xy_list[i]
        if x == 0:
            dp[i + 1][0] = max(dp[i][0] + max(0, y), dp[i][1] + y)
            dp[i + 1][1] = dp[i][1]
        else:
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = max(dp[i][0] + y, dp[i][1])
    return max(dp[-1])


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(5, [(1, 100), (1, 300), (0, -200), (1, 500), (1, 300)]) == 600
    assert solve(4, [(0, -1), (1, -2), (0, -3), (1, -4)]) == 0


if __name__ == "__main__":
    test()
    main()
