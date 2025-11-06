def solve(s):
    m = len(s)
    s_left = ["D", "D", "D"]
    s_list = list(s) + ["D", "D", "D"]
    i = 0
    while i < m + 1:
        # print(i, s_list[i])
        if s_left[-2] == "A" and s_left[-1] == "B" and s_list[i] == "C":
            s_left.pop()
            s_left.pop()
            i += 1
        elif s_left[-1] == "A" and s_list[i] == "B" and s_list[i + 1] == "C":
            s_left.pop()
            i += 2
        elif s_list[i] == "A" and s_list[i + 1] == "B" and s_list[i + 2] == "C":
            i += 3
        else:
            if s_list[i] != "D":
                s_left.append(s_list[i])
            i += 1
    # print("".join(s_left[3:]))
    return "".join(s_left[3:])


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("BAABCBCCABCAC") == "BCAC"
    assert solve("ABCABC") == ""
    assert solve("AAABCABCABCAABCABCBBBAABCBCCCAAABCBCBCC") == "AAABBBCCC"


if __name__ == "__main__":
    test()
    main()
