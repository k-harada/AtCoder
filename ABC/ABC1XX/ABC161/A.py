def solve(x, y, z):
    return z, x, y


def main():
    x, y, z = map(int, input().split())
    res = solve(x, y, z)
    print(z, x, y)


def test():
    assert solve(1, 2, 3) == (3, 1, 2)
    assert solve(100, 100, 100) == (100, 100, 100)


if __name__ == "__main__":
    test()
    main()
