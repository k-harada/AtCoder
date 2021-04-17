def solve(x, y, z):
    res = int(y * z / x)
    if res * x == y * z:
        res -= 1
    return res


def main():
    x, y, z = map(int, input().split())
    res = solve(x, y, z)
    print(res)


def test():
    assert solve(100, 200, 100) == 199
    assert solve(103, 971, 593) == 5590
    assert solve(100, 1, 1) == 0


if __name__ == "__main__":
    test()
    main()
