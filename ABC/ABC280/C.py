def solve(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i + 1
    return len(t)


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("atcoder", "atcorder") == 5
    assert solve("million", "milllion") == 5
    assert solve("vvwvw", "vvvwvw") == 3
    assert solve("vvwvw", "vvwvwc") == 6


if __name__ == "__main__":
    test()
    main()
