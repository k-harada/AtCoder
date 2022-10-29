def f(x):
    g1 = int("".join(sorted(str(x), reverse=True)))
    g2 = int("".join(sorted(str(x))))
    return g1 - g2


def solve(n, k):
    res = n
    for _ in range(k):
        res = f(res)
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(314, 2) == 693
    assert solve(1000000000, 100) == 0
    assert solve(6174, 100000) == 6174


if __name__ == "__main__":
    test()
    main()
