def solve(a, b, c, d):
    if c * d <= b:
        return -1
    else:
        e = c * d - b
        return (a + e - 1) // e


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(5, 2, 3, 2) == 2
    assert solve(6, 9, 2, 3) == -1


if __name__ == "__main__":
    test()
    main()
