MOD = 10 ** 9 + 7


def solve(h, w, k):
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    free = [[0] * 2 for _ in range(w + 1)]
    free[0][0] = 1
    for i in range(w):
        free[i + 1][0] = (free[i][0] + free[i][1]) % MOD
        free[i + 1][1] = free[i][0]

    for i in range(h):
        # stay
        for j in range(w):
            if w - 1 - (j + 1) > 0:
                left = sum(free[w - 1 - (j + 1)])
            else:
                left = 1
            if j - 1 > 0:
                right = sum(free[j - 1])
            else:
                right = 1
            # print(i, j, left, right)
            dp[i + 1][j] += left * right * dp[i][j]
            dp[i + 1][j] %= MOD
        # right
        for j in range(w - 1):
            if w - 1 - (j + 2) > 0:
                left = sum(free[w - 1 - (j + 2)])
            else:
                left = 1
            if j - 1 > 0:
                right = sum(free[j - 1])
            else:
                right = 1
            # print(i, j, left, right)
            dp[i + 1][j + 1] += left * right * dp[i][j]
            dp[i + 1][j + 1] %= MOD
        # left
        for j in range(1, w):
            if w - 1 - (j + 1) > 0:
                left = sum(free[w - 1 - (j + 1)])
            else:
                left = 1
            if j - 2 > 0:
                right = sum(free[j - 2])
            else:
                right = 1
            # print(i, j, left, right)
            dp[i + 1][j - 1] += left * right * dp[i][j]
            dp[i + 1][j - 1] %= MOD
    # print(dp)
    return dp[h][k - 1]


def main():
    h, w, k = map(int, input().split())
    res = solve(h, w, k)
    print(res)


def test():
    assert solve(1, 3, 2) == 1
    assert solve(1, 3, 1) == 2
    assert solve(2, 3, 3) == 1
    assert solve(2, 3, 1) == 5
    assert solve(7, 1, 1) == 1
    assert solve(15, 8, 5) == 437760187


if __name__ == "__main__":
    test()
    main()
