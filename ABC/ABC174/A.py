def solve(x):
    if x >= 30:
        return "Yes"
    else:
        return "No"


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(25) == "No"
    assert solve(30) == "Yes"


if __name__ == "__main__":
    test()
    main()
