def solve(s):
    if s[0] != "<":
        return "No"
    if s[-1] != ">":
        return "No"
    for c in s[1:-1]:
        if c != "=":
            return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("<====>") == "Yes"
    assert solve("==>") == "No"
    assert solve("<>>") == "No"


if __name__ == "__main__":
    test()
    main()
