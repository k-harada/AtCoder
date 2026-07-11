def solve(n, k, ab_list):
    dp = [[[-10 ** 16] * 2 for _1 in range(k + 1)] for _2 in range(n + 1)]
    dp[0][0][0] = 0
    # dp[a][j][0]
    for i in range(n):
        a, b = ab_list[i]
        for j in range(k + 1):
            dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][0] + a)
            if j < k:
                dp[i + 1][j + 1][1] = max(dp[i + 1][j][0], dp[i][j][0] + b)
            dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][1] + b)
            dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][1] + a)
        
    res = max(max([dp[n][j][0] for j in range(k + 1)]), max([dp[n][j][1] for j in range(k + 1)]))
    return res


def main():
    n, k = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, k, ab_list)
    print(res)


def test():
    assert solve(7, 2, [(2, 1), (6, 9), (3, 5), (9, 2), (4, 8), (7, 4), (5, 6)]) == 45
    assert solve(5, 6, [(9, 6), (3, 2), (8, 1), (7, 5), (8, 4)]) == 35
    assert solve(9, 1, [(2, 7), (9, 4), (1, 1), (6, 1), (3, 4), (8, 9), (1, 2), (7, 5), (3, 9)]) == 47


if __name__ == "__main__":
    test()
    main()
