MOD = 998244353


def solve(n):
    res = 0
    m = len(str(n))
    for i in range(1, m):
        x = 9 * (10 ** (i - 1)) % MOD
        res += (1 + x) * x // 2
        res %= MOD
    last = (n - (10 ** (m - 1)) + 1) % MOD
    res += (1 + last) * last // 2
    res %= MOD
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(16) == 73
    assert solve(238) == 13870
    assert solve(999999999999999999) == 762062362


if __name__ == "__main__":
    test()
    main()
