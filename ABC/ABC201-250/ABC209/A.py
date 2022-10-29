def solve(a, b):
    return max(b - a + 1, 0)


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 4) == 3
    assert solve(10, 100) == 91
    assert solve(3, 2) == 0


if __name__ == "__main__":
    test()
    main()
