MOD = 998244353


def solve(n, ab_list):
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n):
        if ab_list[i][0] != ab_list[i - 1][0]:
            dp[i][0] += dp[i - 1][0]
        if ab_list[i][0] != ab_list[i - 1][1]:
            dp[i][0] += dp[i - 1][1]
        if ab_list[i][1] != ab_list[i - 1][0]:
            dp[i][1] += dp[i - 1][0]
        if ab_list[i][1] != ab_list[i - 1][1]:
            dp[i][1] += dp[i - 1][1]
        dp[i][0] %= MOD
        dp[i][1] %= MOD
    res = (dp[-1][0] + dp[-1][1]) % MOD
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(3, [(1, 2), (4, 2), (3, 4)]) == 4
    assert solve(4, [(1, 5), (2, 6), (3, 7), (4, 8)]) == 16


if __name__ == "__main__":
    test()
    main()
