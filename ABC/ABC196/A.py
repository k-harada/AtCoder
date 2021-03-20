def solve(a, b, c, d):
    return b - c


def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve(0, 10, 0, 10) == 10
    assert solve(-100, -100, 100, 100) == -200
    assert solve(-100, 100, -100, 100) == 200


if __name__ == "__main__":
    test()
    main()
