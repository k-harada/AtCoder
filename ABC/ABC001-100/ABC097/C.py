def solve(s, k):
    res_list = []
    for i in range(len(s)):
        for j in range(k):
            res_list.append(s[i:(i + j + 1)])
    res_set = set(res_list)
    res_list_s = list(sorted(list(res_set)))
    # print(res_list_s)
    return res_list_s[k - 1]


def main():
    s = input()
    k = int(input())
    res = solve(s, k)
    print(res)


def test():
    assert solve("aba", 4) == "b"
    assert solve("atcoderandatcodeer", 5) == "andat"
    assert solve("z", 1) == "z"


if __name__ == "__main__":
    test()
    main()
