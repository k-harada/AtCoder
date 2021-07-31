def solve(s):
    if s[0] == s[1] == s[2] == s[3]:
        return "Weak"
    elif int(s[1]) == (int(s[0]) + 1) % 10 and int(s[2]) == (int(s[1]) + 1) % 10 and int(s[3]) == (int(s[2]) + 1) % 10:
        return "Weak"
    else:
        return "Strong"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("7777") == "Weak"
    assert solve("0112") == "Strong"
    assert solve("9012") == "Weak"


if __name__ == "__main__":
    test()
    main()
