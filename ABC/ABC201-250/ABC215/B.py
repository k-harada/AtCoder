def solve(n):
    r = 0
    m = 1
    while 2 * m <= n:
        m *= 2
        r += 1
    return r


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(6) == 2
    assert solve(8) == 3
    assert solve(1) == 0
    assert solve(1000000000000000000) == 59


if __name__ == "__main__":
    test()
    main()
