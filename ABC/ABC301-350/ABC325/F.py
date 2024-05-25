def solve(n, d_list, l1, c1, k1, l2, c2, k2):
    dp = [[10 ** 15] * (k1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for p in range(k1 + 1):
            for q in range(p, k1 + 1):
                r = d_list[i] - (q - p) * l1
                if r > 0:
                    s = r // l2
                    if r % l2 > 0:
                        s += 1
                else:
                    s = 0
                dp[i + 1][q] = min(dp[i + 1][q], dp[i][p] + (q - p) * c1 + s * c2)
    # print(dp[-1])
    res = 10 ** 15
    for i in range(k1 + 1):
        if (dp[-1][i] - i * c1) // c2 <= k2:
            res = min(res, dp[-1][i])
    if res == 10 ** 15:
        res = -1
    return res


def main():
    n = int(input())
    d_list = list(map(int, input().split()))
    l1, c1, k1 = map(int, input().split())
    l2, c2, k2 = map(int, input().split())
    res = solve(n, d_list, l1, c1, k1, l2, c2, k2)
    print(res)


def test():
    assert solve(3, [3, 5, 10], 4, 3, 3, 2, 2, 6) == 17
    assert solve(3, [3, 5, 10], 4, 3, 3, 2, 2, 3) == -1
    assert solve(2, [4, 8], 3, 1, 100, 4, 10000, 100) == 5


if __name__ == "__main__":
    test()
    main()
