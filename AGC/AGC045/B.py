


def solve(s):
    n = len(s)
    # count 0
    # ? -> 1
    res_0 = 0
    cnt_00 = 0
    cnt_01 = 0
    # count 1
    # ? -> 0
    res_1 = 0
    cnt_10 = 0
    cnt_11 = 0
    return 0


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("0??") == 1
    assert solve("0??0") == 2
    assert solve("??00????0??0????0?0??00??1???11?1?1???1?11?111???1") == 4
    assert solve("11?00") == 3
    assert solve("001?100") == 3


if __name__ == "__main__":
    test()
    main()
