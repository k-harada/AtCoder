MOD = 998244353


def solve(n, m):

    if n == 1:
        return m % MOD

    res = n * pow(m, n, MOD)
    res %= MOD
    m_inv = pow(m, MOD - 2, MOD)
    for i in range(1, m + 1):
        a = 1
        b = pow(m, n - 2, MOD)
        for d in range(1, n):
            res -= (a * b * (n - d)) % MOD
            a *= m - i
            a %= MOD
            b *= m_inv
            b %= MOD
        res %= MOD
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(2, 3) == 15
    assert solve(3, 2) == 15
    assert solve(34, 56) == 649717324


if __name__ == "__main__":
    test()
    main()
