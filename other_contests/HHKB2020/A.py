def solve(s, t):
    if s == "Y":
        return t.upper()
    else:
        return t.lower()


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("Y", "a") == "A"
    assert solve("N", "b") == "b"


if __name__ == "__main__":
    test()
    main()
