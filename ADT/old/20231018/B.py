def solve(x, y, n):
    p = n // 3
    q = n % 3
    if y < 3 * x:
        res = p * y + q * x
    else:
        res = n * x
    return res


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
