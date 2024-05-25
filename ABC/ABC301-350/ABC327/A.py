def solve(n, s):
    for i in range(n - 1):
        if s[i] == "b" and s[i + 1] == "a":
            return "Yes"
        elif s[i] == "a" and s[i + 1] == "b":
            return "Yes"
    return "No"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(3, "abc") == "Yes"
    assert solve(2, "ba") == "Yes"
    assert solve(7, "atcoder") == "No"


if __name__ == "__main__":
    test()
    main()
