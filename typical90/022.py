def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(a, b, c):
    d = gcd(gcd(a, b), c)
    res = (a + b + c) // d - 3
    return res


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(2, 2, 3) == 4
    assert solve(2, 2, 4) == 1
    assert solve(1000000000000000000, 999999999999999999, 999999999999999998) == 2999999999999999994


if __name__ == "__main__":
    test()
    main()
