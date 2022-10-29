def solve(a, b, x):
    res = 0
    for k in range(1, 10):
        r = (x - k * b) // a
        r = min(10 ** k - 1, r)
        if r >= 10 ** (k - 1):
            res = r
    if x >= (10 ** 9) * a + b * 10:
        res = 10 ** 9
    return res


def main():
    a, b, x = map(int, input().split())
    res = solve(a, b, x)
    print(res)


def test():
    assert solve(10, 7, 100) == 9
    assert solve(2, 1, 100000000000) == 1000000000
    assert solve(1000000000, 1000000000, 100) == 0


if __name__ == "__main__":
    test()
    main()
