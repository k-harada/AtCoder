def solve(x, y):
    if x - 3 <= y <= x + 2:
        return "Yes"
    else:
        return "No"


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(1, 4) == "No"
    assert solve(99, 96) == "Yes"
    assert solve(100, 1) == "No"


if __name__ == "__main__":
    test()
    main()
