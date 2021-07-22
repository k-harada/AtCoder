def solve(a, b, c):
    if b == max([a, b, c]):
        return b - a + b - c
    elif 2 * b <= a + c:
        if (a + c) % 2 == 0:
            return (a + c) // 2 - b
        else:
            return 1 + (a + c + 1) // 2 - b
    else:
        return 2 * b - a - c


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(4, 8, 10) == 2
    assert solve(10, 3, 4) == 4
    assert solve(1, 2, 3) == 0
    assert solve(1000000000000000, 1, 1000000000000000) == 999999999999999


if __name__ == "__main__":
    test()
    main()
