from bisect import bisect_left


def solve(n, m, ab_list):
    dp = [n + 1] * (n + 2)
    dp[0] = 0
    ab_list_s = list(sorted(ab_list, key=lambda x: (x[0], -x[1])))
    for a, b in ab_list_s:
        k = bisect_left(dp, b)
        dp[k] = b
    # print(dp)
    res = 0
    for i in range(1, n + 1):
        if dp[i] <= n:
            res = i
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(3, 3, [(1, 2), (2, 3), (3, 1)]) == 2
    assert solve(3, 5, [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3)]) == 3
    assert solve(7, 5, [(1, 7), (7, 1), (3, 4), (2, 6), (5, 2)]) == 1


if __name__ == "__main__":
    test()
    main()
