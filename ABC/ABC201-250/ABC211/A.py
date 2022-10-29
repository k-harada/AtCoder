def solve(a, b):
    return (a - b) / 3 + b


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(130, 100) == 110
    assert solve(300, 50) == 133.3333333
    assert solve(123, 123) == 123


if __name__ == "__main__":
    # test()
    main()
