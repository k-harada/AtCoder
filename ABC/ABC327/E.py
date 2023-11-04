import math


def solve(n, p_list):
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    for i in range(n):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] * 0.9 + p_list[i])
    # print(dp[-1])
    res = -1200.0
    q = 1.0
    for i in range(1, n + 1):
        r = dp[-1][i] / q - 1200 / math.sqrt(i)
        q += 0.9 ** i
        res = max(res, r)
        # print(r)
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert abs(solve(3, [1000, 600, 1200]) - 256.735020470879931) < 0.0000001
    assert abs(solve(3, [600, 1000, 1200]) - 261.423219407873376) < 0.0000001
    assert abs(solve(1, [100]) + 1100) < 0.0000001


if __name__ == "__main__":
    test()
    main()
