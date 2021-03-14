MOD = 998244353


def solve(n, m):

    res = n * pow(m, n, MOD)
    res %= MOD
    for d in range(1, n):
        diff = 0
        for i in range(1, m + 1):
            diff += pow(m - i, d - 1, MOD) * pow(m, n - d - 1, MOD)
        res -= diff * (n - d)
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
