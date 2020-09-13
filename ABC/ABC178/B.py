def solve(a, b, c, d):
    return max([a * c, a * d, b * c, b * d])


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(1, 2, 1, 1) == 2
    assert solve(3, 5, -4, -2) == -6
    assert solve(-1000000000, 0, -1000000000, 0) == 1000000000000000000


if __name__ == "__main__":
    test()
    main()
