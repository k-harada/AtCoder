def solve(a, b):
    if a + 1 == b:
        return "Yes"
    elif a == 1 and b == 10:
        return "Yes"
    return "No"


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(4, 5) == "Yes"
    assert solve(3, 5) == "No"
    assert solve(1, 10) == "Yes"


if __name__ == "__main__":
    test()
    main()
