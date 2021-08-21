def solve(s):
    if s == "Hello,World!":
        return "AC"
    else:
        return "WA"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("Hello,World!") == "AC"
    assert solve("Hello,world!") == "WA"
    assert solve("Hello!World!") == "WA"


if __name__ == "__main__":
    test()
    main()
