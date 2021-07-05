def solve(x):
    res = 0
    res += (x // 500) * 1000
    x = x % 500
    res += (x // 5) * 5
    return res


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(1024) == 2020
    assert solve(0) == 0
    assert solve(1000000000) == 2000000000


if __name__ == "__main__":
    test()
    main()
