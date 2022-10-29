def solve(s):
    dp = [0] * 2019
    dp[0] = 1
    r = 0
    for i in range(1, len(s) + 1):
        r += int(s[-i]) * pow(10, i - 1, 2019)
        r %= 2019
        dp[r] += 1
    res = 0
    for r in range(2019):
        res += dp[r] * (dp[r] - 1) // 2
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("1817181712114") == 3
    assert solve("14282668646") == 2
    assert solve("2119") == 0


if __name__ == "__main__":
    test()
    main()
