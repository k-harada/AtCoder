def solve(n, a_list):
    # interval dp
    dp = [[2 * n * 10 ** 6 + 1] * (2 * n) for _ in range(2 * n)]
    for i in range(2 * n - 1):
        dp[i][i + 1] = abs(a_list[i + 1] - a_list[i])
    for k in range(3, 2 * n, 2):
        for i in range(2 * n - k):
            dp[i][i + k] = min([dp[i][p] + dp[p + 1][i + k] for p in range(i + 1, i + k, 2)])
            dp[i][i + k] = min(dp[i][i + k], dp[i + 1][i + k - 1] + abs(a_list[i + k] - a_list[i]))
    # print(dp)
    return dp[0][-1]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [6, 2, 3, 9, 8, 6]) == 2
    assert solve(3, [1, 3, 5, 5, 3, 1]) == 0
    assert solve(4, [1, 2, 4, 8, 16, 32, 64, 128]) == 85


if __name__ == "__main__":
    test()
    main()
