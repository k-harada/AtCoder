def solve(n, m, abc_list):
    g = [[] for _ in range(n)]
    for a, b, c in abc_list:
        g[a - 1].append((b - 1, c))
        g[b - 1].append((a - 1, c))
    dp = [[[-1] * (2 ** n) for _1 in range(n)] for _2 in range(n + 1)]
    for j in range(n):
        dp[0][j][2 ** j] = 0
    for i in range(n):
        for j in range(n):
            for k, d in g[j]:
                for a in range(2 ** n):
                    if dp[i][j][a] >= 0 and a & (2 ** k) == 0:
                        dp[i + 1][k][a + (2 ** k)] = max(dp[i][j][a] + d, dp[i + 1][k][a + (2 ** k)])
    res = 0
    for i in range(n + 1):
        for j in range(n):
            for a in range(2 ** n):
                res = max(res, dp[i][j][a])
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(4, 4, [(1, 2, 1), (2, 3, 10), (1, 3, 100), (1, 4, 1000)]) == 1110
    assert solve(10, 1, [(5, 9, 1)]) == 1
    assert solve(10, 13, [
        (1, 2, 1),
        (1, 10, 1),
        (2, 3, 1),
        (3, 4, 4),
        (4, 7, 2),
        (4, 8, 1),
        (5, 8, 1),
        (5, 9, 3),
        (6, 8, 1),
        (6, 9, 5),
        (7, 8, 1),
        (7, 9, 4),
        (9, 10, 3),
    ]) == 20


if __name__ == "__main__":
    test()
    main()
