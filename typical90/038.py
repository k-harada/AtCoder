def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(a, b):
    c = gcd(a, b)
    res = a * b // c
    if res > 10 ** 18:
        return "Large"
    else:
        return str(res)


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(4, 6) == "12"
    assert solve(1000000000000000000, 3) == "Large"
    assert solve(1000000000000000000, 1) == "1000000000000000000"


if __name__ == "__main__":
    test()
    main()
