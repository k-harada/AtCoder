def solve(n, s, t):
    for i in range(n):
        if s[i] == t[i]:
            pass
        elif s[i] == "1" and t[i] == "l" or s[i] == "l" and t[i] == "1":
            pass
        elif s[i] == "0" and t[i] == "o" or s[i] == "o" and t[i] == "0":
            pass
        else:
            return "No"
    return "Yes"


def main():
    n = int(input())
    s = input()
    t = input()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(3, "l0w", "1ow") == "Yes"
    assert solve(3, "abc", "arc") == "No"
    assert solve(4, "nok0", "n0ko") == "Yes"


if __name__ == "__main__":
    test()
    main()
