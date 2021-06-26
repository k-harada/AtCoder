MOD = 10 ** 9 + 7


def solve(n, a_list):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    a_cum_sum = []
    s = 0
    res = 0
    for i in range(n):
        s += a_list[i]
        a_cum_sum.append(s)
    # print(a_cum_sum)

    for j in range(n):
        for i in range(n - 1, -1, -1):
            k = a_cum_sum[j] % (i + 1)
            m = a_cum_sum[j] % (i + 2)
            nn = k % (i + 1)
            # print(i, j, k, m, nn)
            dp[i + 1][m] = (dp[i + 1][m] + dp[i][nn]) % MOD
            if j == n - 1:
                res = (res + dp[i][nn]) % MOD
        # print(dp)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 2, 3, 4]) == 3
    assert solve(5, [8, 6, 3, 3, 3]) == 5


if __name__ == "__main__":
    test()
    main()
