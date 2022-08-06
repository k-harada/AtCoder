def solve(n, s_list):
    s_dict = dict()
    res_list = []
    for s in s_list:
        if s not in s_dict.keys():
            res_list.append(s)
            s_dict[s] = 1
        else:
            res_list.append(f"{s}({s_dict[s]})")
            s_dict[s] += 1

    return res_list


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, ["newfile", "newfile", "newfolder", "newfile", "newfolder"]) == [
        "newfile", "newfile(1)", "newfolder", "newfile(2)", "newfolder(1)"
    ]


def test_large():
    print(solve(200000, [str(i + 1000000000) for i in range(200000)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
