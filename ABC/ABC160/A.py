def solve(s):
    if s[2] == s[3] and s[4] == s[5]:
        return "Yes"
    else:
        return "No"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("sippuu") == "Yes"
    assert solve("iphone") == "No"
    assert solve("coffee") == "Yes"


if __name__ == "__main__":
    test()
    main()
