def solve(n, s):
    count_dict = dict()
    at_cnt = 0
    cg_cnt = 0
    count_dict[(at_cnt, cg_cnt)] = 1
    for i in range(n):
        if s[i] == "A":
            at_cnt += 1
        elif s[i] == "T":
            at_cnt -= 1
        if s[i] == "C":
            cg_cnt += 1
        elif s[i] == "G":
            cg_cnt -= 1
        if (at_cnt, cg_cnt) in count_dict.keys():
            count_dict[(at_cnt, cg_cnt)] += 1
        else:
            count_dict[(at_cnt, cg_cnt)] = 1
    res = 0
    for v in count_dict.values():
        res += v * (v - 1) // 2
    return res


def main():
    n_str, s = input().split()
    n = int(n_str)
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "AGCT") == 2
    assert solve(4, "ATAT") == 4
    assert solve(10, "AAATACCGCG") == 6


if __name__ == "__main__":
    test()
    main()
