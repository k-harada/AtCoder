def solve(x):
    return 1 - x


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(1) == 0
    assert solve(0) == 1


if __name__ == "__main__":
    test()
    main()
