def solve(s):
    s_list = list(s)
    res = 0
    for c in list("atcoder"):
        i = s_list.index(c)
        res += i
        s_list = s_list[:i] + s_list[i + 1:]
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
