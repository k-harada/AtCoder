from itertools import combinations, permutations


def solve(n, d):
    res = 0
    if n % 2 == 1:
        d = [[0] * n] + d
        n += 1
    dp = [[-10 ** 12] * (2 ** n) for _ in range(n + 1)]
    for i in range(n):
        dp[i][2 ** i] = 0
    pd_list = []
    for p in range(2 ** n):
        di = 0
        for i in range(n):
            if p & (2 ** i) > 0:
                di += 1
        pd_list.append((p, di))
    pd_list = list(sorted(pd_list, key=lambda x: x[1]))
    # print(pd_list)
    for p, di in pd_list:
        for i in range(n):
            if p & (2 ** i) == 0:
                continue
            for j in range(n):
                if p & (2 ** j) == 0:
                    q = p + 2 ** j
                    i_, j_ = min(i, j), max(i, j)
                    if di % 2 == 1:
                        dp[j][q] = max(dp[j][q], dp[i][p] + d[i_][j_ - i_ - 1])
                    else:
                        dp[j][q] = max(dp[j][q], dp[i][p])
        # print(dp)
    # print([dp[i][-1] for i in range(n)])
    res = max([dp[i][-1] for i in range(n)])
    return res


def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, d)
    print(res)


def test():
    assert solve(4, [[1, 5, 4], [7, 8], [6]]) == 13
    assert solve(3, [[1, 2], [3]]) == 3


if __name__ == "__main__":
    test()
    main()
