def solve(n, s):
    dict_1 = dict()
    dict_2 = dict()
    dict_3 = dict()
    for i in range(n):
        a = s[i]
        for k2 in dict_2.keys():
            dict_3[k2 + a] = 1
        for k1 in dict_1.keys():
            dict_2[k1 + a] = 1
        dict_1[a] = 1
    return len(dict_3.keys())


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "0224") == 3
    assert solve(6, "123123") == 17
    assert solve(19, "3141592653589793238") == 329


if __name__ == "__main__":
    test()
    main()
