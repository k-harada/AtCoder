def solve(s, t):
    m = len(s)
    list_1 = []
    list_2 = []
    for i in range(m):
        if s[i] != t[i]:
            if s[i] < t[i]:
                list_2.append(i)
            else:
                list_1.append(i)
    res = [len(list_1) + len(list_2)]
    s_list = list(s)
    for i in list_1:
        s_list[i] = t[i]
        res.append("".join(s_list))
    for i in reversed(list_2):
        s_list[i] = t[i]
        res.append("".join(s_list))
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    for r in res:
        print(r)


def test():
    assert solve("adbe", "bcbc") == [3, "acbe", "acbc", "bcbc"]
    assert solve("abcde", "abcde") == [0]
    assert solve("afwgebrw", "oarbrenq") == [
        8,
        "aawgebrw",
        "aargebrw",
        "aarbebrw",
        "aarbebnw",
        "aarbebnq",
        "aarbeenq",
        "aarbrenq",
        "oarbrenq",
    ]


if __name__ == "__main__":
    test()
    main()
