MOD = 998244353


def solve(s):
    m = len(s)
    if m % 2 == 1:
        return 0
    dp = [[0] * (m // 2 + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i, c in enumerate(s):
        if c == "(":
            for j in range(m // 2):
                dp[i + 1][j + 1] = dp[i][j]
        elif c == ")":
            for j in range(m // 2):
                dp[i + 1][j] = dp[i][j + 1]
        else:
            for j in range(m // 2):
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j] += dp[i][j + 1]
            for j in range(m // 2 + 1):
                dp[i + 1][j] %= MOD
    return dp[m][0]


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("(???(?") == 2
    assert solve(")))))") == 0
    assert solve("??????????????(????????(??????)?????????(?(??)") == 603032273


if __name__ == "__main__":
    test()
    main()
