def solve(n, x, a_list):

    res_min = x - max(a_list)

    for m in range(2, n + 1):
        dp = [[-1] * m for _ in range(m + 1)]
        dp[0][0] = 0
        for a in a_list:
            for p in range(m - 1, -1, -1):
                for q in range(m):
                    if dp[p][q] >= 0:
                        r = (dp[p][q] + a) % m
                        dp[p + 1][r] = max(dp[p + 1][r], dp[p][q] + a)

        d = x % m
        # print(d)
        if dp[m][d] > 0:
            res = (x - dp[m][d]) // m
            res_min = min(res_min, res)
        # print(dp)
    # print(res_min)
    return res_min


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(3, 9999999999, [3, 6, 8]) == 4999999994
    assert solve(1, 1000000000000000000, [1]) == 999999999999999999


if __name__ == "__main__":
    test()
    main()
