# ABC208D
LARGE = 10 ** 18


def solve(n, m, abc_list):

    # Warshall-Floyd Algorithm
    dp = [[LARGE] * (n + 1) for _ in range(n + 1)]
    for a, b, c in abc_list:
        dp[a][b] = c
    for i in range(1, n + 1):
        dp[i][i] = 0

    res = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                if dp[i][j] < LARGE:
                    res += dp[i][j]
    # print(dp)
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [map(int, input().split()) for _ in range(m)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(3, 2, [(1, 2, 3), (2, 3, 2)]) == 25
    assert solve(3, 0, []) == 0


if __name__ == "__main__":
    test()
    main()
