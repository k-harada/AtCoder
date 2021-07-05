def solve(h, w, a, b):
    s = h * w
    dp = [[0] * (2 ** s) for _ in range(a + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            k = i * w + j
            for p in range(2 ** s):
                q = 2 ** k
                if p & q != 0:
                    continue
                for r in range(a):
                    # yoko
                    if j < w - 1:
                        q = 3 * 2 ** k
                        if p & q == 0:
                            # print(p, q)
                            dp[r + 1][p + q] += dp[r][p]
                    # tate
                    if i < h - 1:
                        q = (2 ** w + 1) * (2 ** k)
                        if p & q == 0:
                            # print(p, q)
                            dp[r + 1][p + q] += dp[r][p]
    # print(dp[a])
    return sum(dp[a])


def main():
    h, w, a, b = map(int, input().split())
    res = solve(h, w, a, b)
    print(res)


def test():
    assert solve(2, 2, 1, 2) == 4
    assert solve(3, 3, 4, 1) == 18
    assert solve(4, 4, 8, 0) == 36


if __name__ == "__main__":
    # test()
    main()
