def solve(n, a, b):
    res = n // (a + b) * a
    res += min(n % (a + b), a)
    return res


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(8, 3, 4) == 4
    assert solve(8, 0, 4) == 0
    assert solve(6, 2, 4) == 2


if __name__ == "__main__":
    test()
    main()
