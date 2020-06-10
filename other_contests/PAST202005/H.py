def solve(n, le, x_list, t1, t2, t3):
    is_x = [0] * (le + 1)
    for x in x_list:
        is_x[x] = 1
    # dp
    dp = [le * (t1 + t2 + t3)] * (le + 4)
    dp[0] = 0

    for i in range(le):
        if is_x[i]:
            add = t3
        else:
            add = 0
        # run
        dp[i + 1] = min(dp[i] + t1 + add, dp[i + 1])
        # jump 1
        dp[i + 2] = min(dp[i] + t1 + t2 + add, dp[i + 2])
        # jump 2
        dp[i + 4] = min(dp[i] + t1 + t2 * 3 + add, dp[i + 4])

    res = dp[le]
    # jump_pass
    res_1 = dp[le - 1] + is_x[le - 1] * t3 + (t1 + t2) // 2
    res = min(res, res_1)
    res_2 = dp[le - 2] + is_x[le - 2] * t3 + (t1 + t2) // 2 + t2
    res = min(res, res_2)
    if le > 2:
        res_3 = dp[le - 3] + is_x[le - 3] * t3 + (t1 + t2) // 2 + 2 * t2
        res = min(res, res_3)
    return res


def main():
    n, le = map(int, input().split())
    x_list = list(map(int, input().split()))
    t1, t2, t3 = map(int, input().split())
    res = solve(n, le, x_list, t1, t2, t3)
    print(res)


def test():
    assert solve(2, 5, [1, 4], 2, 2, 20) == 10
    assert solve(4, 5, [1, 2, 3, 4], 2, 20, 100) == 164
    assert solve(10, 19, [1, 3, 4, 5, 7, 8, 10, 13, 15, 17], 2, 1000, 10) == 138


if __name__ == "__main__":
    test()
    main()
