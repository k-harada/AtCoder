def solve(x, y):
    for i in range(x + 1):
        if 2 * x + 2 * i == y:
            return "Yes"
    return "No"


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(3, 8) == "Yes"
    assert solve(2, 100) == "No"
    assert solve(1, 2) == "Yes"


if __name__ == "__main__":
    test()
    main()
