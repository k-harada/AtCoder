def solve(s, t):
    if len(s) > len(t):
        return "No"
    if t[:len(s)] == s:
        return "Yes"
    else:
        return "No"


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
