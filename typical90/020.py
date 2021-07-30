def solve(a, b, c):
    if a < pow(c, b):
        return "Yes"
    else:
        return "No"


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(4, 3, 2) == "Yes"
    assert solve(16, 3, 2) == "No"
    assert solve(8, 3, 2) == "No"


if __name__ == "__main__":
    test()
    main()
