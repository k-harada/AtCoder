def solve(n, t_list, v_list):
    t_max = 2 * sum(t_list)
    v_max = 2 * max(v_list)
    v_limit = [0] * (t_max + 1)
    s = 0
    for i in range(n):
        for _ in range(2 * t_list[i]):
            s += 1
            v_limit[s] = 2 * v_list[i]
    # dp
    dp = [[-10 ** 9] * (v_max + 1) for _ in range(t_max + 1)]
    dp[0][0] = 0

    for t in range(t_max):
        for v in range(v_max + 1):
            # up
            if v + 1 <= v_limit[t + 1]:
                dp[t + 1][v + 1] = max(dp[t][v] + 2 * v + 1, dp[t + 1][v + 1])
            # stay
            if v <= v_limit[t + 1]:
                dp[t + 1][v] = max(dp[t][v] + 2 * v, dp[t + 1][v])
            # down
            if 0 < v <= v_limit[t + 1]:
                dp[t + 1][v - 1] = max(dp[t][v] + 2 * v - 1, dp[t + 1][v - 1])
    res = dp[t_max][0] / 8
    return res


def main():
    n = int(input())
    t_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    res = solve(n, t_list, v_list)
    print(res)


def test():
    assert solve(1, [100], [30]) == 2100
    assert solve(2, [60, 50], [34, 38]) == 2632
    assert solve(3, [12, 14, 2], [6, 2, 7]) == 76
    assert solve(1, [9], [10]) == 20.25


if __name__ == "__main__":
    test()
    main()
