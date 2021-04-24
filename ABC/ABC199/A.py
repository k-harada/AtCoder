def solve(a, b, c):
    if a * a + b * b < c * c:
        return "Yes"
    else:
        return "No"


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(2, 2, 4) == "Yes"
    assert solve(10, 10, 10) == "No"
    assert solve(3, 4, 5) == "No"


if __name__ == "__main__":
    test()
    main()
