def solve(s):
    return s[:3]


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("takahashi") == "tak"
    assert solve("naohiro") == "nao"


if __name__ == "__main__":
    test()
    main()
