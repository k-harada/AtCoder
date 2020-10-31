MOD = 998244353


def solve(a, b, c):
    res = 1
    res *= (a * (a + 1) // 2) % MOD
    res %= MOD
    res *= (b * (b + 1) // 2) % MOD
    res %= MOD
    res *= (c * (c + 1) // 2) % MOD
    res %= MOD
    return res


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(1, 2, 3) == 18
    assert solve(1000000000, 987654321, 123456789) == 951633476


if __name__ == "__main__":
    test()
    main()
