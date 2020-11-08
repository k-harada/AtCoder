def solve(a, b):
    return a * 2 + 100 - b


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(200, 300) == 200
    assert solve(10000, 0) == 20100


if __name__ == "__main__":
    test()
    main()
