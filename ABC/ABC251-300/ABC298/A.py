def solve(n, s):
    if "x" in s:
        return "No"
    elif "o" in s:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "oo--") == "Yes"
    assert solve(3, "---") == "No"
    assert solve(1, "o") == "Yes"
    assert solve(100, "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox") == "No"


if __name__ == "__main__":
    test()
    main()
