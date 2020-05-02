def solve(a, b, c, d):
    while True:
        c -= b
        if c <= 0:
            return "Yes"
        a -= d
        if a <= 0:
            return "No"


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(10, 9, 10, 10) == "No"
    assert solve(46, 4, 40, 5) == "Yes"


if __name__ == "__main__":
    test()
    main()
