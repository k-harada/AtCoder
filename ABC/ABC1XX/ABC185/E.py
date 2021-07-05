def solve(n, m, a_list, b_list):
    dp = [[10 ** 7] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i < n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < m:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            if i < n and j < m:
                if a_list[i] == b_list[j]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
    return dp[n][m]


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(4, 3, [1, 2, 1, 3], [1, 3, 1]) == 2
    assert solve(4, 6, [1, 3, 2, 4], [1, 5, 2, 6, 4, 3]) == 3
    assert solve(5, 5, [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]) == 5


if __name__ == "__main__":
    test()
    main()
