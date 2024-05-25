from heapq import heappush, heappop


def solve(n, a, b, c, d):
    dp = [10 ** 18] * n
    h = [(0, 0)]
    while len(h):
        d_, i = heappop(h)
        if d_ >= dp[i]:
            continue
        dp[i] = d_
        for j in range(n):
            if dp[j] > dp[i] + d[i][j] * a:
                heappush(h, (dp[i] + d[i][j] * a, j))
    # print(dp)
    dq = [10 ** 18] * n
    h = [(0, n - 1)]
    while len(h):
        d_, i = heappop(h)
        if d_ >= dq[i]:
            continue
        dq[i] = d_
        for j in range(n):
            if dq[j] > dq[i] + d[i][j] * b + c:
                heappush(h, (dq[i] + d[i][j] * b + c, j))
    # print(dq)
    res = 10 ** 18
    for i in range(n):
        res = min(res, dp[i] + dq[i])
    return res


def main():
    n, a, b, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, a, b, c, d)
    print(res)


def test():
    assert solve(4, 8, 5, 13, [
        [0, 6, 2, 15],
        [6, 0, 3, 5],
        [2, 3, 0, 13],
        [15, 5, 13, 0]
    ]) == 78
    assert solve(3, 1, 1000000, 1000000, [
        [0, 10, 1],
        [10, 0, 10],
        [1, 10, 0]
    ]) == 1
    assert solve(5, 954257, 954213, 814214, [
        [0, 84251, 214529, 10017, 373342],
        [84251, 0, 91926, 32336, 164457],
        [214529, 91926, 0, 108914, 57762],
        [10017, 32336, 108914, 0, 234705],
        [373342, 164457, 57762, 234705, 0]
    ]) == 168604826785


if __name__ == "__main__":
    test()
    main()
