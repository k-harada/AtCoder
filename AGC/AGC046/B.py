MOD = 998244353


def solve(a, b, c, d):
    dp1 = [[0] * (d + 1) for _ in range(c + 1)]
    dp2 = [[0] * (d + 1) for _ in range(c + 1)]
    dp3 = [[0] * (d + 1) for _ in range(c + 1)]
    dp1[a][b] = 1
    dp2[a][b] = 0
    dp3[a][b] = 0
    for i in range(a + 1, c + 1):
        dp1[i][b] = (pow(b - 1, i - a, MOD) + pow(b - 1, i - a - 1, MOD) * 1 * (i - a)) % MOD
        dp3[i][b] = (pow(b, i - a, MOD) - dp1[i][b]) % MOD
    for j in range(b + 1, d + 1):
        dp1[a][j] = (pow(a - 1, j - b, MOD) + pow(a - 1, j - b - 1, MOD) * 1 * (j - b)) % MOD
        dp2[a][j] = (pow(a, j - b, MOD) - dp1[a][j]) % MOD
    for i in range(a + 1, c + 1):
        for j in range(b + 1, d + 1):
            dp1[i][j] = ((dp1[i - 1][j] + dp2[i - 1][j]) * (j - 1)) % MOD
            dp2[i][j] = (dp2[i][j - 1] * i + dp1[i][j - 1] + dp3[i][j - 1]) % MOD
            dp3[i][j] = (dp3[i - 1][j] * j + dp1[i - 1][j] + dp2[i - 1][j]) % MOD

    # print(dp1, dp2, dp3)
    # print((dp1[c][d] + dp2[c][d] + dp3[c][d]) % MOD)
    return (dp1[c][d] + dp2[c][d] + dp3[c][d]) % MOD


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(1, 1, 2, 2) == 3
    assert solve(1, 1, 3, 3) == 30
    assert solve(2, 1, 3, 4) == 65
    # assert solve(31, 41, 59, 265) == 387222020


if __name__ == "__main__":
    test()
    main()
