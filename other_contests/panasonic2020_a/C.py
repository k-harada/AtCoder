def solve(a, b, c):
    # a + b + 2 * sqrt(a*b) < c
    # 4 * a * b < (c - a - b) ** 2
    if c < a + b:
        return "No"
    if 4 * a * b < (c - a - b) ** 2:
        return "Yes"
    else:
        return "No"


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(2, 3, 9) == "No"
    assert solve(2, 3, 10) == "Yes"


if __name__ == "__main__":
    test()
    main()
