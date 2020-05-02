def solve(s):
    res_dict = dict()
    n = len(s)
    # 1
    for i in range(n):
        k = s[i]
        res_dict[k] = 1
    res_dict["."] = 1
    # 2
    for i in range(n - 1):
        k1 = s[i]
        k2 = s[i + 1]
        res_dict[k1 + k2] = 1
        res_dict[k1 + "."] = 1
        res_dict["." + k2] = 1
    if n >= 2:
        res_dict[".."] = 1
    # 3
    for i in range(n - 2):
        k1 = s[i]
        k2 = s[i + 1]
        k3 = s[i + 2]
        res_dict[k1 + k2 + k3] = 1
        res_dict["." + k2 + k3] = 1
        res_dict[k1 + "." + k3] = 1
        res_dict[k1 + k2 + "."] = 1
        res_dict["." + "." + k3] = 1
        res_dict["." + k2 + "."] = 1
        res_dict[k1 + "." + "."] = 1
    if n >= 3:
        res_dict["..."] = 1
    return len(res_dict)


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ab") == 7
    assert solve("aa") == 6
    assert solve("aabbaabb") == 33


if __name__ == "__main__":
    test()
    main()
