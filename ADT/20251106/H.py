def solve(h, w, a, p):
    p_s = sum(p)
    dp = [[p_s] * w for _ in range(h)]
    dp[h - 1][w - 1] = max(p[-1] - a[h - 1][w - 1], 0)
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i < h - 1:
                dp[i][j] = min(max(0, dp[i + 1][j] + p[i + j] - a[i][j]), dp[i][j])
            if j < w - 1:
                dp[i][j] = min(max(0, dp[i][j + 1] + p[i + j] - a[i][j]), dp[i][j])
    # print(dp)
    return dp[0][0]


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    p = list(map(int, input().split()))
    res = solve(h, w, a, p)
    print(res)


def test():
    assert solve(2, 2, [[3, 2], [4, 1]], [1, 3, 6]) == 2
    assert solve(1, 1, [[5]], [3]) == 0
    assert solve(4, 7, [
        [35, 29, 36, 88, 58, 15, 25],
        [99, 7, 49, 61, 67, 4, 57],
        [96, 92, 3, 49, 49, 36, 90],
        [72, 89, 40, 44, 24, 53, 45],
    ], [55, 43, 23, 71, 77, 6, 94, 19, 27, 21]) == 20


if __name__ == "__main__":
    test()
    main()
