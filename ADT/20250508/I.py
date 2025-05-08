def solve(n, m, edge_list):
    edge_list_s = list(sorted(edge_list))
    left = 0.0
    right = 10000.0
    while left + 0.0000000005 < right:
        mid = (left + right) / 2
        dp = [-10000000000000000] * (n + 1)
        dp[1] = 0.0
        for u, v, b, c in edge_list_s:
            dp[v] = max(dp[v], dp[u] + b - c * mid)
        if dp[n] >= 0.0:
            left = mid
        else:
            right = mid
    # print(left)
    return left


def main():
    n, m = map(int, input().split())
    edge_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, edge_list)
    print(res)


def test():
    assert abs(solve(5, 7, [
        (1, 2, 3, 6),
        (1, 3, 9, 5),
        (2, 3, 1, 5),
        (2, 4, 5, 3),
        (2, 5, 1, 9),
        (3, 4, 4, 8),
        (4, 5, 2, 7)
    ]) - 0.75) <= 10 ** (-9)
    assert abs(solve(3, 3, [
        (1, 3, 1, 1),
        (1, 3, 2, 1),
        (1, 3, 3, 1)
    ]) - 3.0) <= 10 ** (-9)


if __name__ == "__main__":
    test()
    main()
