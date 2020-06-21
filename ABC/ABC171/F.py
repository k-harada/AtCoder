MOD = 10 ** 9 + 7


def solve(k, s):
    res = 0
    factorial = [1] * (2 * 10 ** 6)
    factorial_inv = [1] * (2 * 10 ** 6)
    for i in range(1, 2 * 10 ** 6):
        factorial[i] = factorial[i - 1] * i % MOD
    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(2 * 10 ** 6 - 1, 0, -1):
        factorial_inv[i - 1] = factorial_inv[i] * i % MOD
    # print(factorial[:5])
    # print(factorial_inv[:5])
    for i in range(k + 1):
        left = k - i + len(s) - 1
        right = len(s) - 1
        ncr = (factorial[left] * factorial_inv[right] * factorial_inv[left - right]) % MOD
        add = (ncr * pow(25, k - i, MOD) * pow(26, i, MOD)) % MOD
        res += add
        res %= MOD
    # print(res)
    return res


def main():
    k = int(input())
    s = input()
    res = solve(k, s)
    print(res)


def test():
    assert solve(1, "abc") == 25 + 25 + 25 + 26
    assert solve(5, "oof") == 575111451
    assert solve(37564, "whydidyoudesertme") == 318008117


if __name__ == "__main__":
    test()
    main()
