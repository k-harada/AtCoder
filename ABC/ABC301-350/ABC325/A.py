def solve(s, t):
    return s + " san"


def main():
    s, t = input().split()
    res = solve(s, t)
    print(res)


def test():
    assert solve("Takahashi", "Chokudai") == "Takahashi san"
    assert solve("K", "Eyence") == "K san"


if __name__ == "__main__":
    test()
    main()
