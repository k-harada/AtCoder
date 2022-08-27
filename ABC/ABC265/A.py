def solve(x, y, n):
    if 3 * x >= y:
        return y * (n // 3) + x * (n % 3)
    else:
        return x * n


def main():
    x, y, n = map(int, input().split())
    res = solve(x, y, n)
    print(res)


def test():
    assert solve(10, 25, 10) == 85
    assert solve(10, 40, 10) == 100
    assert solve(100, 100, 2) == 200
    assert solve(100, 100, 100) == 3400


if __name__ == "__main__":
    test()
    main()
