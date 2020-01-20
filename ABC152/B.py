def solve(a, b):
    m = min(a, b)
    n = max(a, b)
    return "".join([str(m)] * n)


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(4, 3) == "3333"
    assert solve(7, 7) == "7777777"


if __name__ == "__main__":
    test()
    main()
