def solve(n, w):
    return n // w


def main():
    n, w = map(int, input().split())
    res = solve(n, w)
    print(res)


def test():
    assert solve(10, 3) == 3
    assert solve(1000, 1) == 1000


if __name__ == "__main__":
    test()
    main()
