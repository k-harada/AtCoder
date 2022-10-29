def solve(v, a, b, c):
    d = a + b + c
    r = v % d
    if r < a:
        return "F"
    elif r < a + b:
        return "M"
    else:
        return "T"


def main():
    v, a, b, c = map(int, input().split())
    res = solve(v, a, b, c)
    print(res)


def test():
    assert solve(25, 10, 11, 12) == "T"
    assert solve(30, 10, 10, 10) == "F"
    assert solve(100000, 1, 1, 1) == "M"


if __name__ == "__main__":
    test()
    main()
