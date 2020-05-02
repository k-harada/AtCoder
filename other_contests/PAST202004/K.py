import numpy as np


def solve(n, s, c_list, d_list):
    # DP
    dp = (10 ** 15) * np.ones((n + 1, n // 2 + 1), dtype=np.int)
    dp[0, 0] = 0
    for i in range(n):
        if s[i] == "(":
            dp[i + 1, 1:] = np.minimum(dp[i, :-1], dp[i + 1, 1:])  # keep
            dp[i + 1, :-1] = np.minimum(dp[i, 1:] + c_list[i], dp[i + 1, :-1])  # reverse
            dp[i + 1, :] = np.minimum(dp[i, :] + d_list[i], dp[i + 1, :])  # delete
        else:
            dp[i + 1, 1:] = np.minimum(dp[i, :-1] + c_list[i], dp[i + 1, 1:])  # reverse
            dp[i + 1, :-1] = np.minimum(dp[i, 1:], dp[i + 1, :-1])  # keep
            dp[i + 1, :] = np.minimum(dp[i, :] + d_list[i], dp[i + 1, :])  # delete
    return dp[-1, 0]


def main():
    n = int(input())
    s = input()
    c_list = list(map(int, input().split()))
    d_list = list(map(int, input().split()))
    res = solve(n, s, c_list, d_list)
    print(res)


def test():
    assert solve(3, "))(", [3, 5, 7], [2, 6, 5]) == 8
    assert solve(1, "(", [10], [20]) == 20
    assert solve(10, "))())((()(", [13, 18, 17, 3, 20, 20, 6, 14, 14, 2], [20, 1, 19, 5, 2, 19, 2, 19, 9, 4]) == 18
    assert solve(4, "()()", [17, 8, 3, 19], [5, 3, 16, 3]) == 0


if __name__ == "__main__":
    test()
    main()
