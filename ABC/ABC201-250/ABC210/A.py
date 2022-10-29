def solve(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y


def main():
    n, a, x, y = map(int, input().split())
    res = solve(n, a, x, y)
    print(res)


def test():
    assert solve(5, 3, 20, 15) == 90
    assert solve(10, 10, 100, 1) == 1000


if __name__ == "__main__":
    test()
    main()
