def solve(s):
    return s[1:] + s[0]


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abc") == "bca"
    assert solve("aab") == "aba"


if __name__ == "__main__":
    test()
    main()
