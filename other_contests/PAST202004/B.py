def solve(s):
    a = s.count("a")
    b = s.count("b")
    c = s.count("c")
    m = max(a, b, c)
    if a == m:
        return "a"
    elif b == m:
        return "b"
    else:
        return "c"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abbc") == "b"
    assert solve("cacca") == "c"
    assert solve("b") == "b"
    assert solve("babababacaca") == "a"


if __name__ == "__main__":
    test()
    main()
