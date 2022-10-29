def solve(n, k):
    res = 0
    while n > 0:
        n = n // k
        res += 1
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(11, 2) == 4
    assert solve(1010101, 10) == 7
    assert solve(314159265, 3) == 18


if __name__ == "__main__":
    test()
    main()
