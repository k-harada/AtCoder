def solve(a, b, c):
    if a % c == 0:
        return a
    else:
        d = a - (a % c) + c
        if d <= b:
            return d
        else:
            return -1


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(123, 456, 100) == 200
    assert solve(630, 940, 314) == -1


if __name__ == "__main__":
    test()
    main()
