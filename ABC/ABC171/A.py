def solve(s):
    if s.upper() == s:
        return "A"
    else:
        return "a"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("B") == "A"
    assert solve("a") == "a"


if __name__ == "__main__":
    test()
    main()
