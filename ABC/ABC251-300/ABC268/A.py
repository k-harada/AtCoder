def solve(a, b, c, d, e):
    return len({a, b, c, d, e})


def main():
    a, b, c, d, e = map(int, input().split())
    res = solve(a, b, c, d, e)
    print(res)


def test():
    assert solve(31, 9, 24, 31, 24) == 3
    assert solve(0, 0, 0, 0, 0) == 1


if __name__ == "__main__":
    test()
    main()
