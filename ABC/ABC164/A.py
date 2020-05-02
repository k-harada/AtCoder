def solve(s, w):
    if w >= s:
        return "unsafe"
    else:
        return "safe"


def main():
    s, w = map(int, input().split())
    res = solve(s, w)
    print(res)


def test():
    assert solve(4, 5) == "unsafe"
    assert solve(100, 2) == "safe"
    assert solve(10, 10) == "unsafe"


if __name__ == "__main__":
    test()
    main()
