def solve(x):
    return 100 - x % 100


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(140) == 60
    assert solve(1000) == 100


if __name__ == "__main__":
    test()
    main()
