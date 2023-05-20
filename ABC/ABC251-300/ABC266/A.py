def solve(s):
    a = (len(s) + 1) // 2
    return s[a - 1]


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("atcoder") == "o"
    assert solve("a") == "a"


if __name__ == "__main__":
    test()
    main()
