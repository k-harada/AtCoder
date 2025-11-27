LARGE = 998244353


def solve(n, a_list):
    dp = [0] * (n + 1)
    dp[n] = a_list[n - 1] % LARGE
    s = a_list[n - 1] % LARGE
    n_inv = pow(n, LARGE - 2, LARGE)
    for i in range(n - 1, -1, -1):
        if i > 0:
            dp[i] = s * n_inv + a_list[i - 1]
            dp[i] %= LARGE
            s += dp[i]
        else:
            dp[i] = s * n_inv
            dp[i] %= LARGE
    # print(dp)
    return dp[0]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 2, 6]) == 776412280
    assert solve(1, [998244352]) == 998244352
    assert solve(9, [
        3, 14, 159, 2653, 58979,
        323846, 2643383, 27950288, 419716939
    ]) == 545252774


if __name__ == "__main__":
    test()
    main()
