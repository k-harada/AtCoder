def solve(a, b):
    d = b - a
    while True:
        count = 0
        e = (a // d) * d
        if a <= e <= b:
            count += 1
        if a <= e + d <= b:
            count += 1
        if a <= e + 2 * d <= b:
            count += 1
        if count >= 2:
            return d
        d -= 1


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 4) == 2
    assert solve(199999, 200000) == 1
    assert solve(101, 139) == 34


if __name__ == "__main__":
    test()
    main()
