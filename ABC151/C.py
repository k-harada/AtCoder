def solve(n, m, p_list, s_list):

    res_ac = 0
    res_wa = 0

    ac_dict = dict()
    wa_dict = dict()

    for i in range(m):
        p = p_list[i]
        s = s_list[i]

        if s == "AC":
            if p not in ac_dict.keys():
                ac_dict[p] = 1
                res_ac += 1
                if p in wa_dict.keys():
                    res_wa += wa_dict[p]
        else:
            if p not in wa_dict.keys():
                wa_dict[p] = 1
            else:
                wa_dict[p] += 1
    return str(res_ac) + " " + str(res_wa)


def main():
    n, m = map(int, input().split())
    p_list = [0] * m
    s_list = ["AC"] * m
    for i in range(m):
        p, s = input().split()
        p_list[i] = int(p)
        s_list[i] = s
    res = solve(n, m, p_list, s_list)
    print(res)


def test():
    assert solve(2, 5, [1, 1, 2, 2, 2], ["WA", "AC", "WA", "AC", "WA"]) == "2 2"
    assert solve(100000, 3, [7777, 7777, 7777], ["AC", "AC", "AC"]) == "1 0"
    assert solve(6, 0, [], []) == "0 0"


if __name__ == "__main__":
    test()
    main()
