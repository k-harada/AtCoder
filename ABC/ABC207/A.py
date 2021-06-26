def solve(a, b, c):
    return a + b + c - min([a, b, c])


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(3, 4, 5) == 9
    assert solve(6, 6, 6) == 12
    assert solve(99, 99, 98) == 198


if __name__ == "__main__":
    test()
    main()
