MOD = 998244353


def solve(n, m):
    dp = [[[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][m][m][m] = 1
    for i in range(n):
        for m1 in range(m + 1):
            for m2 in range(m + 1):
                for m3 in range(m + 1):
                    for c in range(min(m, m3 + 1)):
                        n1 = min(c, m1)
                        if c > m1:
                            n2 = min(c, m2)
                        else:
                            n2 = m2
                        if c > m2:
                            n3 = min(c, m3)
                        else:
                            n3 = m3
                        dp[i + 1][n1][n2][n3] += dp[i][m1][m2][m3]
                        dp[i + 1][n1][n2][n3] %= MOD
    res = 0
    for m1 in range(m):
        for m2 in range(m):
            for m3 in range(m):
                res += dp[n][m1][m2][m3]
    res %= MOD
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(4, 5) == 135
    assert solve(3, 4) == 4
    assert solve(111, 3) == 144980434


if __name__ == "__main__":
    test()
    main()
