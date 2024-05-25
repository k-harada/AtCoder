def solve(n):
    if n < 10 ** 3:
        return n
    elif n < 10 ** 4:
        return (n // (10 ** 1)) * (10 ** 1)
    elif n < 10 ** 5:
        return (n // (10 ** 2)) * (10 ** 2)
    elif n < 10 ** 6:
        return (n // (10 ** 3)) * (10 ** 3)
    elif n < 10 ** 7:
        return (n // (10 ** 4)) * (10 ** 4)
    elif n < 10 ** 8:
        return (n // (10 ** 5)) * (10 ** 5)
    elif n < 10 ** 9:
        return (n // (10 ** 6)) * (10 ** 6)
    else:
        return -1


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(20230603) == 20200000
    assert solve(0) == 0
    assert solve(304) == 304
    assert solve(500600) == 500000


if __name__ == "__main__":
    test()
    main()
