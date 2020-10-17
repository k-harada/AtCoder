def solve(n, a, b):
    return n - a + b


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(100, 1, 2) == 101
    assert solve(100, 2, 1) == 99
    assert solve(100, 1, 1) == 100


if __name__ == "__main__":
    test()
    main()
