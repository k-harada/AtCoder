def solve(n, k, h_list):
    if k == n:
        return 0
    # dp table
    large = sum(h_list) + 1
    dp = [[large] * n for _ in range(n + 1)]
    dp[1][0] = h_list[0]
    # update
    for i in range(1, n):
        for s in range(2, n + 1):
            dp[s][i] = min([dp[s - 1][j] + max(0, h_list[i] - h_list[j]) for j in range(i)])
        dp[1][i] = h_list[i]
    # print(dp)
    return min(dp[n - k])


def main():
    n, k = map(int, input().split())
    h_list = list(map(int, input().split()))
    res = solve(n, k, h_list)
    print(res)


def test():
    assert solve(4, 1, [2, 3, 4, 1]) == 3
    assert solve(6, 2, [8, 6, 9, 1, 2, 1]) == 7
    assert solve(10, 0, [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 4999999996


if __name__ == "__main__":
    # test()
    main()
