DUAL_DICT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def solve(m, s_list):
    res_list = []
    for s in s_list:
        t = "".join([DUAL_DICT[c] for c in reversed(s)])
        res_list.append(t)
    return res_list


def main():
    m = int(input())
    s_list = [input() for _ in range(m)]
    res_list = solve(m, s_list)
    for res in res_list:
        print(res)


def test():
    assert solve(6, ["CATAGAACGACTATT", "TA", "GCGGCTTTTTGAAGCGT", "TACCTTGATCA", "GGCGTGCATAG", "T"]) == [
        "AATAGTCGTTCTATG",
        "TA",
        "ACGCTTCAAAAAGCCGC",
        "TGATCAAGGTA",
        "CTATGCACGCC",
        "A"
    ]


if __name__ == "__main__":
    test()
    main()
