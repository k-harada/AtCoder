def solve(a, b, c, d):
    if abs(a - c) <= d:
        return "Yes"
    elif abs(a - b) <= d and abs(b - c) <= d:
        return "Yes"
    return "No"


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(4, 7, 9, 3) == "Yes"
    assert solve(100, 10, 1, 2) == "No"
    assert solve(10, 10, 10, 1) == "Yes"
    assert solve(1, 100, 2, 10) == "Yes"


if __name__ == "__main__":
    test()
    main()
