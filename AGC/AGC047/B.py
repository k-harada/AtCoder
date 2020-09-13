def solve(n, s_list):
    s_list_s = sorted(s_list, key=lambda x: -len(x))
    s_list_s_rev = [s[::-1] for s in s_list_s]

    alphabet_dict = dict()
    for i in range(n):
        alphabet_dict[i] = dict()

    sub_sequence_dict = dict()
    for i in range(n):
        s = s_list_s_rev[i]
        sub = ""
        for j in range(len(s)):
            if sub not in sub_sequence_dict.keys():
                sub_sequence_dict[sub] = []
            sub_sequence_dict[sub].append((i, j))
            sub += s[j]

    return 0


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    # assert solve(2, ["a" * 50000, "a" * 50000]) == 0
    d = []
    s = ""
    for i in range(1000000):
        s = "a" * i
        d.append(s)

    print(0)


if __name__ == "__main__":
    test()
    main()
