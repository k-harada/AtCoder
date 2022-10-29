from itertools import permutations


def solve(s, k):
    u_list = []
    for u in permutations(s):
        u_list.append("".join(u))
    u_list_s = list(sorted(list(set(u_list))))
    return u_list_s[k - 1]


def main():
    s, k_ = input().split()
    k = int(k_)
    res = solve(s, k)
    print(res)


def test():
    assert solve("aab", 2) == "aba"
    assert solve("baba", 4) == "baab"
    assert solve("ydxwacbz", 40320) == "zyxwdcba"


if __name__ == "__main__":
    test()
    main()
