def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solve(a, b):
    return lcm(a, b)


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 3) == 6
    assert solve(123, 456) == 18696
    assert solve(10000, 99999) == 999990000


if __name__ == "__main__":
    test()
    main()
