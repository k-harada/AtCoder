def solve(h, w):
    if h == 1 or w == 1:
        return 1
    return (h * w + 1) // 2


def main():
    h, w = map(int, input().split())
    res = solve(h, w)
    print(res)


def test():
    assert solve(4, 5) == 10
    assert solve(7, 3) == 11
    assert solve(1000000000, 1000000000) == 500000000000000000


if __name__ == "__main__":
    test()
    main()
