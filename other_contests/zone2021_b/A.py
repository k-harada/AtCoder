def solve(n, s_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13 = dict()
    for i in range(26):
        rot13[alphabet[i]] = alphabet[(i + 13) % 26]
    res_list = []
    for s in s_list:
        res = ""
        for c in s:
            res += rot13[c]
        res_list.append(res)
    return res_list


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res_list = solve(n, s_list)
    for res in res_list:
        print(res)


def test():
    assert solve(2, ["aiueo", "kakikukeko"]) == ["nvhrb", "xnxvxhxrxb"]


if __name__ == "__main__":
    test()
    main()
