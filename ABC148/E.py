def solve(n):
    if n % 2 == 1:
        return 0
    else:
        m = n // 2
        res = 0
        while m > 0:
            m = m // 5
            res += m
        return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(12) == 1
    assert solve(5) == 0
    assert solve(1000000000000000000) == 124999999999999995


if __name__ == "__main__":
    test()
    main()
