def solve(n, s):
    if s[n - 1] == "o":
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "oooxoox") == "No"
    assert solve(7, "ooooooo") == "Yes"


if __name__ == "__main__":
    test()
    main()
