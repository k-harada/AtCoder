MOD = 998244353


def solve(n, m, k):
    if m % k != 0:
        return 0

    size = 2 * n - k
    factorial = [1] * (size + 1)
    factorial_inv = [1] * (size + 1)
    for i in range(1, size + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(size, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res = 0

    for i in range(n - k + 1 + 1):
        c = factorial[n - k + 1] * factorial_inv[i] * factorial_inv[n - k + 1 - i]
        c *= (-1) ** i
        c %= MOD
        p = k * i
        if p > (m // k):
            continue
        # print(i)
        h = factorial_inv[2 * n - k]
        # print(h)
        # print(2 * n - k)
        for j in range(2 * n - k):
            # print(m // k - p - j + 2 * n - k)
            h *= (m // k - p - j + 2 * n - k) % MOD
            h %= MOD
        # print(c, h)
        res += c * h
        res %= MOD
        # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    res = solve(n, m, k)
    print(res)


def test():
    assert solve(3, 2, 2) == 5
    assert solve(100, 998244353, 100) == 0
    assert solve(2000, 545782618661124208, 533) == 908877889
    assert solve(2000, 2000, 2000) == 2001


def test_large():
    print(solve(2050, 10000000000, 4))


if __name__ == "__main__":
    test()
    # test_large()
    main()
