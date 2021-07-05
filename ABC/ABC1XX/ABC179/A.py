def solve(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("apple") == "apples"
    assert solve("bus") == "buses"
    assert solve("box") == "boxs"


if __name__ == "__main__":
    test()
    main()
