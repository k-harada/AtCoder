MOD = 998244353


def solve(n, a_list):
    n_inv = [1] + [pow(i, MOD -2, MOD) for i in range(1, n + 1)]
    dp = [0] + a_list
    s = a_list[-1]
    for i in range(n - 1, -1, -1):
        dp[i] += s * n_inv[n]
        dp[i] %= MOD
        s += dp[i]
        s %= MOD
    return dp[0]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 2, 6]) == 776412280
    assert solve(1, [998244352]) == 998244352
    assert solve(9, [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939]) == 545252774


if __name__ == "__main__":
    test()
    main()
