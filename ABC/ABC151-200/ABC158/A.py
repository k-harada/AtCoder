def solve(s):
    if s == "AAA" or s == "BBB":
        return "No"
    else:
        return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ABA") == "Yes"
    assert solve("BBA") == "Yes"
    assert solve("BBB") == "No"


if __name__ == "__main__":
    test()
    main()
