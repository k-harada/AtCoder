from itertools import permutations, combinations_with_replacement
from collections import defaultdict


def solve(n, m, s_list, t_list):

    key_dict = defaultdict(int)
    for t in t_list:
        key_dict[t] = 1

    total_len = 0
    for s in s_list:
        total_len += len(s)
    total_len += n - 1

    if total_len > 16:
        return "-1"

    if n == 1:
        s = s_list[0]
        if s in t_list or len(s) <= 2:
            return "-1"
        else:
            return s

    for p in permutations(s_list):
        for c in combinations_with_replacement(list(range(n)), 16 - total_len):
            c_list = [0] * n
            for c_ in c:
                c_list[c_] += 1
            res = ""
            for i in range(n - 1):
                res += p[i]
                res += "_" * (c_list[i] + 1)
            res += p[-1]
            if key_dict[res] == 0:
                # print(res)
                return res

    return "-1"


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(n)]
    t_list = [input() for _ in range(m)]
    res = solve(n, m, s_list, t_list)
    print(res)


def test():
    assert solve(1, 1, ["chokudai"], ["chokudai"]) == "-1"
    assert solve(2, 2, ["choku", "dai"], ["chokudai", "choku_dai"]) == "choku________dai"
    assert solve(2, 2, ["chokudai", "atcoder"], ["chokudai_atcoder", "atcoder_chokudai"]) == "-1"
    assert solve(4, 4, ["ab", "cd", "ef", "gh"], ["hoge", "fuga", "_____", "_ab_cd_ef_gh_"]) == "ab______cd_ef_gh"


def test_large():

    print(solve(8, 1, ["a", "b", "c", "d", "e", "f", "g", "h"], ["ah"]))


if __name__ == "__main__":
    # test()
    main()
