def solve(n, m):
    r = pow(10, n, m * m)
    s = r // m
    return s % m


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(1, 2) == 1
    assert solve(2, 7) == 0
    assert solve(1000000000000000000, 9997) == 9015


if __name__ == "__main__":
    test()
    main()
