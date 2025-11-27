def solve(a, b, c):
    m = max([a, b, c])
    if m * 2 == a + b + c:
        return "Yes"
    elif a == b == c:
        return "Yes"
    else:
        return "No"


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(3, 8, 5) == "Yes"
    assert solve(2, 2, 2) == "Yes"
    assert solve(1, 2, 4) == "No"


if __name__ == "__main__":
    test()
    main()
