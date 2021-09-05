def solve(s, t):
    if s < t:
        return "Yes"
    else:
        return "No"


def main():
    s, t = input().split()
    res = solve(s, t)
    print(res)


def test():
    assert solve("abc", "atcoder") == "Yes"
    assert solve("arc", "agc") == "No"
    assert solve("a", "aa") == "Yes"


if __name__ == "__main__":
    test()
    main()
