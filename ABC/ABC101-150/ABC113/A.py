def solve(x, y):
    return x + y // 2


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(81, 58) == 110
    assert solve(4, 54) == 31


if __name__ == "__main__":
    test()
    main()
