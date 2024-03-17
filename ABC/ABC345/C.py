from collections import Counter


def solve(s):
    n = len(s)
    c = Counter(list(s))
    res = n * (n - 1) // 2
    flag = 0
    for k in c.keys():
        v = c[k]
        if v >= 2:
            flag = 1
        res -= v * (v - 1) // 2
    res += flag
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abc") == 3
    assert solve("aaaaa") == 1


if __name__ == "__main__":
    test()
    main()
