def solve(a, b, n):
    if n >= b - 1:
        return a * (b - 1) // b
    else:
        return a * n // b


def main():
    a, b, n = map(int, input().split())
    res = solve(a, b, n)
    print(res)


def test():
    assert solve(5, 7, 4) == 2
    assert solve(11, 10, 9) == 9


if __name__ == "__main__":
    test()
    main()
