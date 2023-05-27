def solve(x, y, z, s):
    m = len(s)
    dp = [[10 ** 18] * 2 for _ in range(m + 1)]
    dp[0][0] = 0
    dp[0][1] = z
    for i in range(m):
        if s[i] == "A":
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + y)
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + x)
        else:
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + x)
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + y)
        dp[i + 1][0] = min(dp[i + 1][0], dp[i + 1][1] + z)
        dp[i + 1][1] = min(dp[i + 1][1], dp[i + 1][0] + z)
    # print(dp)
    return min(dp[-1][0], dp[-1][1])


def main():
    x, y, z = map(int, input().split())
    s = input()
    res = solve(x, y, z, s)
    print(res)


def test():
    assert solve(1, 3, 3, "AAaA") == 9
    assert solve(1, 1, 100, "aAaAaA") == 6
    assert solve(1, 2, 4, "aaAaAaaAAAAaAaaAaAAaaaAAAAA") == 40


if __name__ == "__main__":
    test()
    main()
