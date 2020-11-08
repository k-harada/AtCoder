def solve(n, x, a_list):

    dp = [[0] * 2 for _ in range(n)]

    # count_just
    count_just = [0] * n
    x_temp = x
    for i in range(n - 1):
        count_just[i] = (x_temp % a_list[i + 1]) // a_list[i]
        x_temp -= count_just[i] * a_list[i]
    count_just[-1] = x_temp // a_list[-1]

    # count_max
    count_max = [0] * n
    for i in range(n - 1):
        count_max[i] = a_list[i + 1] // a_list[i]
    count_max[-1] = x // a_list[-1] + 1

    # dp[i][0]: enough after ith coin
    # dp[i][1]: not enough after ith coin
    dp[0][0] = 1
    for i in range(n - 1):
        if count_just[i] < count_max[i] - 1:
            dp[i + 1][0] = dp[i][0] + dp[i][1]
        else:
            dp[i + 1][0] = dp[i][0]
        if count_just[i] > 0:
            dp[i + 1][1] = dp[i][0] + dp[i][1]
        else:
            dp[i + 1][1] = dp[i][1]
    return dp[n - 1][0] + dp[n - 1][1]


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(3, 9, [1, 5, 10]) == 3
    assert solve(5, 198, [1, 5, 10, 50, 100]) == 5
    assert solve(4, 44, [1, 4, 20, 100]) == 4


if __name__ == "__main__":
    test()
    main()
