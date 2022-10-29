MOD = 998244353


def solve(n, s):

    v_list = [0] * n
    for i, c in enumerate(s):
        k = "ABCDEFGHIJ".index(c)
        v_list[i] = k

    dp = [[[0] * 1024 for __ in range(11)] for _ in range(n + 1)]
    dp[0][10][0] = 1
    for i in range(n):
        k = v_list[i]

        for v in range(1024):
            for w in range(11):
                dp[i + 1][w][v] = dp[i][w][v]

        for v in range(1024):
            if v & (2 ** k) == 0:
                for w in range(11):
                    dp[i + 1][k][v | (2 ** k)] += dp[i][w][v]
                dp[i + 1][k][v | (2 ** k)] %= MOD

        for v in range(1024):
            dp[i + 1][k][v] += dp[i][k][v]
            dp[i + 1][k][v] %= MOD
        # print(dp[i][k])
    res = sum([sum(dp[-1][k]) for k in range(10)]) % MOD
    # print(res)
    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "BGBH") == 13
    assert solve(100, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIEIJEIJIJCGCCFGIEBIHFCGFBFAEJIEJAJJHHEBBBJJJGJJJCCCBAAADCEHIIFEHHBGF") == 330219020


if __name__ == "__main__":
    test()
    main()
