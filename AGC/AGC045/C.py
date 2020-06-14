MOD = 10 ** 9 + 7


def solve(n, a, b):
    if a == 1 or b == 1:
        return pow(2, n, MOD)
    if a <= b:
        # last 1 * b
        pass

    return 0


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
