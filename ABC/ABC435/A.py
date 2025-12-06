def solve(n):
    return n * (n + 1) // 2


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(5) == 15
    assert solve(1) == 1
    assert solve(29) == 435


if __name__ == "__main__":
    test()
    main()
