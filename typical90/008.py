MOD = 10 ** 9 + 7


def solve(n, s):
    # atcoder
    dp = [0] * 8
    dp[0] = 1
    for c in s:
        if c == "a":
            dp[1] = (dp[1] + dp[0]) % MOD
        elif c == "t":
            dp[2] = (dp[2] + dp[1]) % MOD
        elif c == "c":
            dp[3] = (dp[3] + dp[2]) % MOD
        elif c == "o":
            dp[4] = (dp[4] + dp[3]) % MOD
        elif c == "d":
            dp[5] = (dp[5] + dp[4]) % MOD
        elif c == "e":
            dp[6] = (dp[6] + dp[5]) % MOD
        elif c == "r":
            dp[7] = (dp[7] + dp[6]) % MOD
        # print(dp)
    return dp[7]


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(10, "attcordeer") == 4
    assert solve(41, "btwogablwetwoiehocghiewobadegwhoihegnldir") == 2
    assert solve(
        140, "aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr"
    ) == 279999993


if __name__ == "__main__":
    test()
    main()
