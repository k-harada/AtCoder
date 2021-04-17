MOD = 10 ** 9 + 7


def solve(n, p):
    res = (p - 1) * pow(p - 2, n - 1, MOD)
    return res % MOD


def main():
    n, p = map(int, input().split())
    res = solve(n, p)
    print(res)


def test():
    assert solve(3, 3) == 2
    assert solve(3, 2) == 0
    assert solve(45108, 2571593) == 224219544


if __name__ == "__main__":
    test()
    main()
