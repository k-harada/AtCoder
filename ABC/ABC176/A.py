def solve(n, x, t):
    if n % x == 0:
        return t * (n // x)
    else:
        return t * (n // x + 1)


def main():
    n, x, t = map(int, input().split())
    res = solve(n, x, t)
    print(res)


def test():
    assert solve(20, 12, 6) == 12
    assert solve(1000, 1, 1000) == 1000000


if __name__ == "__main__":
    test()
    main()
