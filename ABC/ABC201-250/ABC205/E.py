MOD = 10 ** 9 + 7


def solve(n, m, k):
    if n > m + k:
        return 0

    factorial = [1] * (n + m + 1)
    factorial_inv = [1] * (n + m + 1)
    for i in range(1, n + m + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n + m, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res_1 = (factorial[n + m] * (factorial_inv[n] * factorial_inv[m] % MOD)) % MOD
    if n <= k:
        res_2 = 0
    else:
        res_2 = (factorial[n + m] * (factorial_inv[n - k - 1] * factorial_inv[m + k + 1] % MOD)) % MOD

    res = (res_1 - res_2) % MOD
    return res


def main():
    n, m, k = map(int, input().split())
    res = solve(n, m, k)
    print(res)


def test():
    assert solve(2, 3, 1) == 9
    assert solve(1, 0, 0) == 0
    assert solve(1000000, 1000000, 1000000) == 192151600


if __name__ == "__main__":
    test()
    main()