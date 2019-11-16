LARGE = 10 ** 9 + 7


def solve(x, y):
    if (x + y) % 3 != 0:
        return 0
    z = (x + y) // 3
    if x < z or y < z:
        return 0
    # zC(x-z)
    r = min(x - z, y - z)
    res = 1
    for i in range(r):
        res *= z - i
        res *= pow(i + 1, LARGE - 2, LARGE)
        res %= LARGE
    return res


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(3, 3) == 2
    assert solve(2, 2) == 0
    assert solve(999999, 999999) == 151840682


if __name__ == "__main__":
    test()
    main()
