def solve(a, b):
    if a <= b <= 6 * a:
        return "Yes"
    else:
        return "No"


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 11) == "Yes"
    assert solve(2, 13) == "No"
    assert solve(100, 600) == "Yes"


if __name__ == "__main__":
    test()
    main()
