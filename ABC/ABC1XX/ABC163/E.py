from heapq import heappop, heappush
import numpy as np


def solve(n, a_list):
    h = []
    for i in range(n):
        heappush(h, (-a_list[i], i))
    # dp
    dp = (-10 ** 18) * np.ones((n + 1, n + 1), dtype=np.int)
    dp[0, 0] = 0
    for i in range(n):
        a, k = heappop(h)
        # add left
        dp[i + 1, 1:] = np.maximum(dp[i, :-1] + (-a) * np.abs(k - np.arange(n)), dp[i + 1, 1:])
        # add right
        # for j in range(n):
        #    dp[i + 1, j] = max(dp[i, j] + (-a) * abs(n - 1 - (i - j) - k), dp[i + 1, j])
        dp[i + 1, :-1] = np.maximum(dp[i, :-1] + (-a) * np.abs(k - np.arange(n - 1 - i, n + n - 1 - i)), dp[i + 1, :-1])

    # print(dp)
    res = dp[-1, :].max()
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 3, 4, 2]) == 20
    assert solve(6, [5, 5, 6, 1, 1, 1]) == 58
    assert solve(6, [8, 6, 9, 1, 2, 1]) == 85
    # print(solve(2000, [0] * 2000))


if __name__ == "__main__":
    test()
    main()
