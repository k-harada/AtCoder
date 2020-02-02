def solve(s):
    if s.isdigit():
        return int(s) * 2
    else:
        return "error"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("678") == 1356
    assert solve("abc") == "error"
    assert solve("0x8") == "error"
    assert solve("012") == 24


if __name__ == "__main__":
    test()
    main()
