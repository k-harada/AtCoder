def solve(a, b):
    return a * b / 100


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(45, 200) == 90
    assert solve(37, 450) == 166.5
    assert solve(0, 1000) == 0
    assert solve(50, 0) == 0


if __name__ == "__main__":
    test()
    main()
