def solve(h, w):
    if h == 1 or w == 1:
        return h * w
    return ((h + 1) // 2) * ((w + 1) // 2)


def main():
    h, w = map(int, input().split())
    res = solve(h, w)
    print(res)


def test():
    assert solve(2, 3) == 2
    assert solve(3, 4) == 4
    assert solve(3, 6) == 6


if __name__ == "__main__":
    test()
    main()
