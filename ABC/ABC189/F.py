def solve(n, m, k, a_list):
    if m == 1:
        if k == 0:
            return n
        else:
            return -1
    straight = 1
    for i in range(k - 1):
        if a_list[i] + 1 == a_list[i + 1]:
            straight += 1
        else:
            straight = 1
        if straight == m:
            return -1
    dp = [[0] * 2 for _ in range(n + m)]
    s0 = 0
    s1 = 0
    for i in range(n - 1, -1, -1):
        if i not in a_list:
            dp[i][0] = s0 + 1
            dp[i][1] = s1
        else:
            dp[i][0] = 0
            dp[i][1] = 1
        s0 += (dp[i][0] - dp[i + m][0]) / m
        s1 += (dp[i][1] - dp[i + m][1]) / m
    res = dp[0][0] / (1 - dp[0][1])
    # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    print(res)


def test():
    assert solve(2, 2, 0, []) == 1.5
    assert solve(2, 2, 1, [1]) == 2.0
    assert solve(100, 6, 10, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert abs(solve(100000, 2, 2, [2997, 92458]) - 201932.2222) < 0.0001


if __name__ == "__main__":
    test()
    main()
