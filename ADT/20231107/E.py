from itertools import permutations


def solve(s, k):
    candidates = []
    for p in permutations(list(s)):
        candidates.append("".join(p))
    candidates_unique = list(set(candidates))
    res = list(sorted(candidates_unique))[k - 1]
    return res


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
