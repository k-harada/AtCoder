def solve(s, t):
    len_d = len(s) - len(t)
    res = len(t)
    for d in range(len_d + 1):
        r = 0
        for i in range(len(t)):
            if t[i] != s[i + d]:
                r += 1
        res = min(res, r)
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve('cabacc', 'abc') == 1
    assert solve('codeforces', 'atcoder') == 6


if __name__ == "__main__":
    test()
    main()
