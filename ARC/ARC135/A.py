MOD = 998244353


def solve(x):
    c = 1
    y = x
    while y > 3:
        y = y // 2
        c *= 2
    a = x - y * c
    b = c - a
    r = pow(y, b, MOD) * pow(y + 1, a, MOD)
    r %= MOD
    return r


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(15) == 192
    assert solve(3) == 3
    assert solve(100) == 824552442


if __name__ == "__main__":
    test()
    main()
