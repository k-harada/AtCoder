def solve(s):
    for i, c in enumerate(s):
        if c.upper() == c:
            return i + 1
    return 0


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("aBc") == 2
    assert solve("xxxxxxXxxx") == 7
    assert solve("Zz") == 1


if __name__ == "__main__":
    test()
    main()
