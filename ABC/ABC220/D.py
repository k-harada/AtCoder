MOD = 998244353


def solve(n, a_list):
    dp = [[0] * 10 for _ in range(n)]
    dp[0][a_list[0]] = 1
    for i in range(n - 1):
        for j in range(10):
            dp[i + 1][(j + a_list[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j * a_list[i + 1]) % 10] += dp[i][j]
        for j in range(10):
            dp[i + 1][j] %= MOD
    return dp[-1]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [2, 7, 6]) == [1, 0, 0, 0, 2, 1, 0, 0, 0, 0]
    assert solve(5, [0, 1, 2, 3, 4]) == [6, 0, 1, 1, 4, 0, 1, 1, 0, 2]


if __name__ == "__main__":
    test()
    main()
