def solve(n, m, x, t, d):
    if x <= m:
        return t
    else:
        return t - (x - m) * d


def main():
    n, m, x, t, d = map(int, input().split())
    res = solve(n, m, x, t, d)
    print(res)


def test():
    assert solve(38, 20, 17, 168, 3) == 168
    assert solve(1, 0, 1, 3, 2) == 1
    assert solve(100, 10, 100, 180, 1) == 90


if __name__ == "__main__":
    test()
    main()
