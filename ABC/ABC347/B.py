def solve(s):
    n = len(s)
    res_list = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            res_list.append(s[i:j])
    res = len(set(res_list))
    # print(res_list)
    # print(res)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("yay") == 5
    assert solve("aababc") == 17
    assert solve("abracadabra") == 54


if __name__ == "__main__":
    test()
    main()
