def solve(r):
    if r < 1200:
        return "ABC"
    elif r < 2800:
        return "ARC"
    else:
        return "AGC"


def main():
    r = int(input())
    res = solve(r)
    print(res)


def test():
    assert solve(1199) == "ABC"
    assert solve(1200) == "ARC"
    assert solve(4208) == "AGC"


if __name__ == "__main__":
    test()
    main()
