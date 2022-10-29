def solve(n):
    if "7" in list(str(n)):
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(117) == "Yes"
    assert solve(123) == "No"
    assert solve(777) == "Yes"


if __name__ == "__main__":
    test()
    main()
