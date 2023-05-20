MOD = 998244353


def solve(a, b, c, d, e, f):
    res = ((((a * b) % MOD) * c) % MOD) - ((((d * e) % MOD) * f) % MOD)
    res %= MOD
    return res


def main():
    a, b, c, d, e, f = map(int, input().split())
    res = solve(a, b, c, d, e, f)
    print(res)


def test():
    assert solve(2, 3, 5, 1, 2, 4) == 22
    assert solve(1, 1, 1000000000, 0, 0, 0) == 1755647
    assert solve(
        1000000000000000000, 1000000000000000000, 1000000000000000000,
        1000000000000000000, 1000000000000000000, 1000000000000000000
    ) == 0


if __name__ == "__main__":
    test()
    main()
