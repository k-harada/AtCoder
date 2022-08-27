MOD = 998244353


def solve(n, d, p, q):
    dp = [[[0] * (d + 1) for _1 in range(n + 1)] for _2 in range(n + 1)]
    dp[0][0][0] = 1
    match = 0
    for i in range(n):
        di = abs(p[i] - q[i])
        if di == 0:
            match += 1
            for j in range(i + 1):
                for k in range(d + 1):
                    dp[i + 1][j][k] = dp[i][j][k]
        else:
            for j in range(i + 1):
                # 0, 1, 1, ..., 1, 0
                s = 0
                for k in range(d + 1):
                    if k >= di:
                        s -= dp[i][j][k - di]
                    dp[i + 1][j][k] += s
                    dp[i + 1][j][k] %= MOD
                    s += dp[i][j][k]
                    # just
                    dp[i + 1][j + 1][k] += dp[i][j][k]
                    if k + di <= d:
                        dp[i + 1][j + 1][k + di] += dp[i][j][k]

    # print(dp)
    double = [[0] * (d + 1) for _ in range(n + 2)]
    double[0][0] = 1
    for j in range(n + 1):
        double[j + 1][0] = 1
        for k in range(1, d + 1):
            double[j + 1][k] = double[j + 1][k - 1] + double[j][k]
            double[j + 1][k] %= MOD

    d_sum = sum([abs(p[i] - q[i]) for i in range(n)])
    res = [0] * (d + 1)
    for j in range(n + 1):
        for k in range(d + 1):
            m = d_sum - k
            if m > d:
                continue
            p = max(k, m)
            q = d - p
            for x in range(q + 1):
                res[p + x] += dp[n][j][k] * double[j][x]
            # print(j, k, double[j + 1][q])
        for k in range(d + 1):
            res[k] %= MOD
    # print(double)
    # print(dp[n])
    # print(res)

    true_double = [[0] * (d + 1) for _ in range(n + 2)]
    true_double[0][0] = 1
    for j in range(n + 1):
        true_double[j + 1][0] = 1
        for k in range(1, d + 1):
            true_double[j + 1][k] = true_double[j + 1][k - 1] + true_double[j][k] + true_double[j][k - 1]
            true_double[j + 1][k] %= MOD
    # print(true_double)

    weight = 0
    r = 0
    for k in range(d + 1):
        weight += true_double[match][k]
        weight %= MOD
        r += res[d - k] * weight
        r %= MOD
    # print(r)
    return r


def main():
    n, d = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    res = solve(n, d, p, q)
    print(res)


def test():
    assert solve(1, 5, [0], [3]) == 8
    assert solve(3, 10, [2, 6, 5], [2, 1, 2]) == 632
    assert solve(10, 100, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]) == 145428186


if __name__ == "__main__":
    test()
    main()
