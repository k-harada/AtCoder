MOD = 998244353


def solve(n, m, a, b, c, d, e, f, xy_list):
    dp = [[[0] * (n + 1) for _1 in range(n + 1)] for _2 in range(n + 1)]
    dp[0][0][0] = 1

    ng_dict = dict()
    for x, y in xy_list:
        ng_dict[f"{x} {y}"] = 1

    for t in range(n):
        for i in range(t + 2):
            for j in range(t + 2):
                # check if ok
                x = a * i + c * j + e * (t + 1 - i - j)
                y = b * i + d * j + f * (t + 1 - i - j)
                if f"{x} {y}" in ng_dict.keys():
                    continue
                dp[t + 1][i][j] += dp[t][i][j]
                dp[t + 1][i][j] += dp[t][i - 1][j]
                dp[t + 1][i][j] += dp[t][i][j - 1]
                dp[t + 1][i][j] %= MOD
    res = 0
    for i in range(n + 1):
        for j in range(n + 1):
            res += dp[n][i][j]
    res %= MOD
    # print(dp)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    a, b, c, d, e, f = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, a, b, c, d, e, f, xy_list)
    print(res)


def test():
    assert solve(2, 2, 1, 1, 1, 2, 1, 3, [(1, 2), (2, 2)]) == 5
    assert solve(10, 3, -1, -1, 1, 1, -1, 1, [(-1, -1), (1, 1), (-1, 1)]) == 0
    assert solve(300, 0, 0, 0, 1, 0, 0, 1, []) == 292172978


if __name__ == "__main__":
    # test()
    main()
