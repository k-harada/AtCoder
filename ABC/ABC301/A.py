def solve(n, s):
    t = s.count("T")
    a = n - t
    if t > a:
        return "T"
    elif t < a:
        return "A"
    elif s[-1] == "T":
        return "A"
    else:
        return "T"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "TTAAT") == "T"
    assert solve(6, "ATTATA") == "T"
    assert solve(1, "A") == "A"


if __name__ == "__main__":
    test()
    main()
