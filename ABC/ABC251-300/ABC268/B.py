def solve(s, t):
    if len(s) > len(t):
        return "No"
    for i, c in enumerate(s):
        if c != t[i]:
            return "No"
    return "Yes"


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("atco", "atcoder") == "Yes"
    assert solve("code", "atcoder") == "No"
    assert solve("abc", "abc") == "Yes"
    assert solve("aaaa", "aa") == "No"


if __name__ == "__main__":
    test()
    main()
