def solve(a, b, x, y):
    if a == b:
        return x
    if a > b:
        return x + (a - b - 1) * min(y, 2 * x)
    else:
        return x + (b - a) * min(y, 2 * x)


def main():
    a, b, x, y = map(int, input().split())
    res = solve(a, b, x, y)
    print(res)


def test():
    assert solve(2, 1, 1, 5) == 1
    assert solve(1, 2, 100, 1) == 101
    assert solve(1, 100, 1, 100) == 199


if __name__ == "__main__":
    test()
    main()
