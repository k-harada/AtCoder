def solve(a, b, c, d):
    return a * d - b * c


def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(1, 2, 3, 4) == -2
    assert solve(0, -1, 1, 0) == 1
    assert solve(100, 100, 100, 100) == 0


if __name__ == "__main__":
    test()
    main()
