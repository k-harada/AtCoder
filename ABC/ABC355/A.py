def solve(a, b):
    if a == b:
        return -1
    else:
        return 6 - a - b


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(1, 2) == 3
    assert solve(1, 1) == -1
    assert solve(3, 1) == 2


if __name__ == "__main__":
    test()
    main()
