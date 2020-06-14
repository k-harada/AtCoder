def solve(x1, x2, x3, x4, x5):
    for i, x in enumerate([x1, x2, x3, x4, x5]):
        if x == 0:
            return i + 1
    return 0


def main():
    x1, x2, x3, x4, x5 = map(int, input().split())
    res = solve(x1, x2, x3, x4, x5)
    print(res)


def test():
    assert solve(0, 2, 3, 4, 5) == 1
    assert solve(1, 2, 0, 4, 5) == 3


if __name__ == "__main__":
    test()
    main()
