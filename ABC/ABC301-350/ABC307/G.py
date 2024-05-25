def solve(n, a_list):
    d = sum(a_list) % n
    r = sum(a_list) // n
    dp = [[10 ** 18] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    dif = 0
    for i in range(n):
        # i番目をrにする
        for j in range(d + 1):
            x = abs(a_list[i] + dif - j - r)
            dp[i + 1][j] = min(dp[i][j] + x, dp[i + 1][j])
        # i番目をr + 1にする
        for j in range(d):
            x = abs(a_list[i] + dif - j - r - 1)
            dp[i + 1][j + 1] = min(dp[i][j] + x, dp[i + 1][j + 1])
        dif += a_list[i] - r
    # print(dp)
    return dp[-1][d]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 7, 6]) == 4
    assert solve(3, [-2, -5, -2]) == 2
    assert solve(5, [1, 1, 1, 1, -7]) == 13


if __name__ == "__main__":
    test()
    main()
