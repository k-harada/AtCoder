def solve(s):
    if s[-2:] == "er":
        return "er"
    else:
        return "ist"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("atcoder") == "er"
    assert solve("tourist") == "ist"
    assert solve("er") == "er"


if __name__ == "__main__":
    test()
    main()
