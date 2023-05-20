def solve(s, n):
    m = 0
    k = len(s)
    for i, c in enumerate(s):
        if c == "1":
            m += 2 ** (k - i - 1)
    if m > n:
        return -1
    d = n - m
    for i, c in enumerate(s):
        if c == "?":
            if 2 ** (k - i - 1) <= d:
                m += 2 ** (k - i - 1)
                d = n - m
    # print(m)
    return m


def main():
    s = input()
    n = int(input())
    res = solve(s, n)
    print(res)


def test():
    assert solve("?0?", 2) == 1
    assert solve("101", 4) == -1
    assert solve("?0?", 1000000000000000000) == 5


if __name__ == "__main__":
    test()
    main()
