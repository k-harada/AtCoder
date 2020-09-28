def solve(a, b, c, d):
    if c <= a <= d:
        return "Yes"
    if c <= b <= d:
        return "Yes"
    if a <= c <= b:
        return "Yes"
    if a <= d <= b:
        return "Yes"
    return "No"


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(10, 30, 20, 40) == "Yes"
    assert solve(10, 20, 30, 40) == "No"


if __name__ == "__main__":
    test()
    main()
