def solve(s, t):
    u = s
    for i in range(len(s)):
        u = u[1:] + u[0]
        if u == t:
            return "Yes"
    return "No"


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("tokyo", "kyoto") == "Yes"
    assert solve("abc", "arc") == "No"
    assert solve("aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaab") == "Yes"


if __name__ == "__main__":
    test()
    main()
