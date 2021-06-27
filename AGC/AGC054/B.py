MOD = 998244353


def solve(n, w_list):
    w_sum = sum(w_list)
    if w_sum % 2 == 1:
        return 0
    dp = [[0] * (w_sum // 2 + 1) for _ in range(n // 2 + 1)]
    dp[0][0] = 1
    for i in range(n):
        for k in range(n // 2, 0, -1):
            for w in range(w_sum // 2 + 1 - w_list[i]):
                if dp[k - 1][w] > 0:
                    dp[k][w + w_list[i]] += dp[k - 1][w]
                    dp[k][w + w_list[i]] %= MOD
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    res = 0
    for k in range(n // 2 + 1):
        res += 2 * factorial[k] * factorial[n - k] * dp[k][w_sum // 2]
    if n % 2 == 0:
        k = n // 2
        res -= factorial[k] * factorial[n - k] * dp[k][w_sum // 2]
    res %= MOD
    return res


def main():
    n = int(input())
    w_list = list(map(int, input().split()))
    res = solve(n, w_list)
    print(res)


def test():
    assert solve(3, [1, 1, 2]) == 4
    assert solve(4, [1, 2, 3, 8]) == 0
    assert solve(4, [1, 2, 3, 4]) == 8
    assert solve(20, [2, 8, 4, 7, 5, 3, 1, 2, 4, 1, 2, 5, 4, 3, 3, 8, 1, 7, 8, 2]) == 373835282


if __name__ == "__main__":
    test()
    main()
