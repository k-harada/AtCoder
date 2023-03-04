def solve(s):
    return s.upper()


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abc") == "ABC"
    assert solve("a") == "A"
    assert solve("abcdefghjiklnmoqprstvuwxyz") == "ABCDEFGHJIKLNMOQPRSTVUWXYZ"


if __name__ == "__main__":
    test()
    main()
