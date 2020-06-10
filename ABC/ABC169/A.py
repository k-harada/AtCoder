def solve(a, b):
    return a * b


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 5) == 10
    assert solve(100, 100) == 10000


if __name__ == "__main__":
    test()
    main()
