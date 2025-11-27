def solve(s):
    res = "2" * s.count("2")
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("20250222") == "22222"
    assert solve("2") == "2"
    assert solve("22222000111222222") == "22222222222"


if __name__ == "__main__":
    test()
    main()
