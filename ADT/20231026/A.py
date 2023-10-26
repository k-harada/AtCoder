def solve(x):
    if x % 100 == 0 and x > 0:
        return "Yes"
    else:
        return "No"


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(500) == "Yes"
    assert solve(40) == "No"
    assert solve(0) == "No"


if __name__ == "__main__":
    test()
    main()
