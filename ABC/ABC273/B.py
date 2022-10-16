def solve(x, k):
    res = x
    for i in range(k):
        d = 10 ** (i + 1)
        res, mod = (res // d) * d, res % d
        if mod * 2 >= d:
            res += d
    return res


def main():
    x, k = map(int, input().split())
    res = solve(x, k)
    print(res)


def test():
    assert solve(2048, 2) == 2100
    assert solve(1, 15) == 0
    assert solve(999, 3) == 1000
    assert solve(314159265358979, 12) == 314000000000000


if __name__ == "__main__":
    test()
    main()
