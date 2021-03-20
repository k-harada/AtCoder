def solve(n):
    len_n = len(str(n))
    if len_n % 2 == 1:
        return 10 ** (len_n // 2) - 1
    else:
        d = 10 ** (len_n // 2)
        left = n // d
        right = n % d
        if left <= right:
            return left
        else:
            return left - 1


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(33) == 3
    assert solve(1333) == 13
    assert solve(1312) == 12
    assert solve(100) == 9
    assert solve(999) == 9
    assert solve(10000000) == 999


if __name__ == "__main__":
    test()
    main()
