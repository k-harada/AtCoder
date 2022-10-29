def solve(s, a, b):
    return s[:a - 1] + s[b - 1] + s[a:b - 1] + s[a - 1] + s[b:]


def main():
    s = input()
    a, b = map(int, input().split())
    res = solve(s, a, b)
    print(res)


def test():
    assert solve("chokudai", 3, 5) == "chukodai"
    assert solve("aa", 1, 2) == "aa"
    assert solve("aaaabbbb", 1, 8) == "baaabbba"


if __name__ == "__main__":
    test()
    main()
