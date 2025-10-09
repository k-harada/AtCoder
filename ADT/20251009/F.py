def solve(n, s_list):
    res = []
    res_dict = dict()
    for s in s_list:
        if s in res_dict.keys():
            res_dict[s] += 1
            res.append(f"{s}({res_dict[s]})")
        else:
            res_dict[s] = 0
            res.append(s)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [
        "newfile",
        "newfile",
        "newfolder",
        "newfile",
        "newfolder"
    ]) == [
        "newfile",
        "newfile(1)",
        "newfolder",
        "newfile(2)",
        "newfolder(1)"
    ]
    assert solve(11, ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == [
        "a", "a(1)", "a(2)", "a(3)", "a(4)", "a(5)", "a(6)", "a(7)", "a(8)", "a(9)", "a(10)"
    ]


if __name__ == "__main__":
    test()
    main()
