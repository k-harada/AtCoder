def solve(n, s_list):
    s_list_0 = [s for s in s_list if s[0] != "!"]
    s_list_1 = [s[1:] for s in s_list if s[0] == "!"]
    set_0 = set(s_list_0)
    set_1 = set(s_list_1)
    list_intersect = list(set_0.intersection(set_1))
    if len(list_intersect) == 0:
        return "satisfiable"
    else:
        return list_intersect[0]


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(6, ["a", "!a", "b", "!c", "d", "!d"]) == "a"
    assert solve(10, ["red", "red", "red", "!orange", "yellow", "!blue", "cyan", "!green", "brown", "!gray"]) == "satisfiable"


if __name__ == "__main__":
    # test()
    main()
