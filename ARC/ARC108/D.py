MOD = 10 ** 9 + 7


def solve(n, c_aa, c_ab, c_ba, c_bb):
    if n <= 3:
        return 1
    # switch so that c_aa == 'A'
    if c_ab == 'B':
        if c_bb == 'A':
            c_aa = 'B'
        else:
            c_aa = 'A'
        if c_ba == 'A':
            c_ba = 'B'
        else:
            c_ba = 'A'
    # trivial case
    if c_aa == 'A':
        return 1
    # c_ab == 'A', c_aa == 'B'
    if c_ba == 'A':
        # A_XXX_AB no 'BB'
        dp = [[0, 0] for _ in range(n - 2)]
        dp[0][0] = 1
        for i in range(1, n - 2):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][1] = dp[i - 1][0]
        return (dp[-1][0] + dp[-1][1]) % MOD
    # c_ab == 'A', c_aa == 'B', c_ba == 'B'
    # A_XXX_AB: X: any
    return pow(2, n - 3, MOD)


def main():
    n = int(input())
    c_aa = input()
    c_ab = input()
    c_ba = input()
    c_bb = input()
    res = solve(n, c_aa, c_ab, c_ba, c_bb)
    print(res)


def test():
    assert solve(4, 'A', 'B', 'B', 'A') == 2
    assert solve(1000, 'B', 'B', 'B', 'B') == 1


if __name__ == "__main__":
    test()
    main()
