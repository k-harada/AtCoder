def solve(s):
    t = list(s).copy()
    res = 0
    for i, c in enumerate("atcoder"):
        j = t.index(c)
        t = t[:j] + t[j + 1:]
        t = t[:i] + [c] + t[i:]
        res += (j - i)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("catredo") == 8
    assert solve("atcoder") == 0
    assert solve("redocta") == 21


if __name__ == "__main__":
    test()
    main()
