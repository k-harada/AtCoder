MOD = 998244353


def solve(n, a_list, b_list):
    ab_list = [(a, b) for a, b in zip(a_list, b_list)]
    ab_list_s = list(sorted(ab_list, key=lambda x: x[0]))
    a_list_s = [ab[0] for ab in ab_list_s]
    b_list_s = [ab[1] for ab in ab_list_s]
    dp = [[0] * 5001 for _ in range(n + 1)]
    dp[0][0] = 1
    res = 0
    for i in range(n):
        for v in range(a_list_s[i] - b_list_s[i] + 1):
            res += dp[i][v]
        res %= MOD
        for v in range(5001):
            dp[i + 1][v] = dp[i][v]
        for v in range(5001 - b_list_s[i]):
            dp[i + 1][v + b_list_s[i]] += dp[i][v]
            dp[i + 1][v + b_list_s[i]] %= MOD
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(2, [3, 1], [1, 2]) == 2
    assert solve(2, [1, 1], [2, 2]) == 0


if __name__ == "__main__":
    test()
    main()
