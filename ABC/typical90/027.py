def solve(n, s_list):
    s_dict = dict()
    res = []
    for i, s in enumerate(s_list):
        if s not in s_dict.keys():
            res.append(i + 1)
        s_dict[s] = 1
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, ["e869120", "atcoder", "e869120", "square1001", "square1001"]) == [1, 2, 4]
    assert solve(4, ["taro", "hanako", "yuka", "takashi"]) == [1, 2, 3, 4]
    assert solve(10, ["square869120"] * 10) == [1]


if __name__ == "__main__":
    test()
    main()
