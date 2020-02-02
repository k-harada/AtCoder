def solve(s, t):
    return t + s


def main():
    s, t = input().split()
    res = solve(s, t)
    print(res)


def test():
    assert solve("oder", "atc") == "atcoder"
    assert solve("humu", "humu") == "humuhumu"


if __name__ == "__main__":
    test()
    main()
