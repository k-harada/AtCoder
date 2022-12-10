def solve(n, m):
    ncr = [[0] * n for _ in range(n)]
    ncr[0][0] = 1
    for i in range(1, n):
        ncr[i][0] = 1
        for j in range(1, n):
            ncr[i][j] = (ncr[i - 1][j - 1] + ncr[i - 1][j]) % m
    # print(ncr)
    pow2 = [0] * (n * n // 2)
    pow2[0] = 1
    for i in range(1, len(pow2)):
        pow2[i] = (pow2[i - 1] * 2) % m
    # print(pow2)
    pow2_1 = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            pow2_1[i][j] = (pow2_1[i][j - 1] * (pow2[i] - 1)) % m
    dp = [[0] * n for _ in range(n)]
    # dp[i][j]: iこ使って、最大距離がj個
    dp[1][1] = 1
    for i in range(2, n):
        for i0 in range(1, i):
            for j in range(n):
                if dp[i0][j] == 0:
                    continue
                # i - i0個の点を選んで、j個のうちいくつかとくっつけさせる
                # 点を選ぶ
                add = dp[i0][j]
                add *= ncr[n - 1 - i0][i - i0]
                # j個と結ぶ
                add *= pow2_1[j][i - i0]
                add %= m
                # i - i0内でつなぐ
                add *= pow2[(i - i0) * (i - i0 - 1) // 2]
                add %= m
                dp[i][i - i0] += add
                dp[i][i - i0] %= m
                # print(i, i0, j, add)
        # print(dp)
    # print(dp)
    res = 0
    for j in range(n):
        res += dp[-1][j] * pow2_1[j][1]
        res %= m
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(4, 1000000000) == 8
    assert solve(3, 100000000) == 1
    assert solve(500, 987654321) == 610860515


if __name__ == "__main__":
    # test()
    main()
