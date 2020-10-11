def solve(a, b, c, d):
    s = a + b + c + d
    if s % 2 == 1:
        return "No"
    h = s // 2
    if a == h:
        return "Yes"
    elif b == h:
        return "Yes"
    elif c == h:
        return "Yes"
    elif d == h:
        return "Yes"
    elif a + b == h:
        return "Yes"
    elif a + c == h:
        return "Yes"
    elif a + d == h:
        return "Yes"

    return "No"


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(1, 3, 2, 4) == "Yes"
    assert solve(1, 2, 4, 8) == "No"


if __name__ == "__main__":
    test()
    main()
