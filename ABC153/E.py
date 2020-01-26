def solve(h, n, a_list, b_list):
    res = 10 ** 10
    dp = [10 ** 10] * h
    dp[0] = 0
    for i in range(h):
        for j in range(n):
            if i + a_list[j] < h:
                dp[i + a_list[j]] = min(dp[i + a_list[j]], dp[i] + b_list[j])
            else:
                res = min(res, dp[i] + b_list[j])
    return res


def main():
    h, n = map(int, input().split())
    a_list = [0] * n
    b_list = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        a_list[i] = a
        b_list[i] = b
    res = solve(h, n, a_list, b_list)
    print(res)


def test():
    assert solve(9, 3, [8, 4, 2], [3, 2, 1]) == 4
    assert solve(100, 6, [1, 2, 3, 4, 5, 6], [1, 3, 9, 27, 81, 243]) == 100
    assert solve(
        9999, 10,
        [540, 691, 700, 510, 415, 551, 587, 619, 588, 176],
        [7550, 9680, 9790, 7150, 5818, 7712, 8227, 8671, 8228, 2461]
    ) == 139815


if __name__ == "__main__":
    test()
    main()
