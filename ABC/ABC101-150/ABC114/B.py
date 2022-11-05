def solve(s):
    d_min = 999
    for i in range(len(s) - 2):
        a = int(s[i:(i + 3)])
        d_min = min(d_min, abs(a - 753))
    # print(d_min)
    return d_min


def main():
    s = input()
    res = solve(s)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve("1234567876") == 34
    assert solve("35753") == 0
    assert solve("1111111111") == 642


if __name__ == "__main__":
    test()
    main()
