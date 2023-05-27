def solve(n, k, c_list, p_list):
    p_inv = [0] * n
    for i, p in enumerate(p_list):
        p_inv[p - 1] = i
    # dp[i][a][b]: 区間a, bを 2**i未満で処理するのにかかる費用
    dp = [[[10 ** 15] * n for _1 in range(n)] for _2 in range(k + 1)]

    for a in range(n):
        for i in range(k + 1):
            dp[i][a][a] = 0
        for b in range(a + 1, n):
            if p_inv[b - 1] < p_inv[b]:
                dp[0][a][b] = 0
            else:
                break

    for i in range(1, k + 1):
        for a in range(n):
            for b in range(a + 1, n):
                dp[i][a][b] = dp[i - 1][a][b]
                for d in range(a, b):
                    if p_inv[d] < p_inv[d + 1]:
                        dp[i][a][b] = min(
                            dp[i][a][b], dp[i - 1][a][d] + dp[i - 1][d + 1][b] + (b - d) * c_list[k - i]
                        )
                    else:
                        dp[i][a][b] = min(
                            dp[i][a][b], dp[i - 1][a][d] + dp[i - 1][d + 1][b] + (b - d) * c_list[k - i]
                        )
    # print(dp[0])
    # print(dp[1])
    # print(dp[k])
    # print(dp[k][0][n - 1])
    if dp[k][0][n - 1] == 1000000000000000:
        return -1
    else:
        return dp[k][0][n - 1]


def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    p_list = list(map(int, input().split()))
    res = solve(n, k, c_list, p_list)
    print(res)


def test():
    assert solve(4, 1, [3], [3, 1, 2, 4]) == 6
    assert solve(4, 1, [3], [4, 3, 2, 1]) == -1
    assert solve(20, 10, [
        874735445, 684260477, 689935252, 116941558, 915603029,
        923404262, 843759669, 656978932, 286318130, 255195090
    ], [
        11, 15, 20, 10, 6, 8, 18, 2, 12, 4, 9, 13, 19, 3, 16, 7, 14, 17, 5, 1
    ]) == 7372920743


if __name__ == "__main__":
    test()
    main()
