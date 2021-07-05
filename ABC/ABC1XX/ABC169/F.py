MOD = 998244353


def solve(n, s, a_list):
    dp = [[0] * 3001 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        a = a_list[i]
        for v in range(3001):
            dp[i + 1][v] = (dp[i][v] * 2) % MOD
        for v in range(3001):
            if v + a > 3000:
                break
            dp[i + 1][v + a] = (dp[i + 1][v + a] + dp[i][v]) % MOD
    # print(dp[n])
    return dp[n][s]


def main():
    n, s = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, s, a_list)
    print(res)


def test():
    assert solve(3, 4, [2, 2, 4]) == 6
    assert solve(5, 8, [9, 9, 9, 9, 9]) == 0
    assert solve(10, 10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 3296


if __name__ == "__main__":
    test()
    main()
