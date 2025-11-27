def solve(s, t):
    res = []
    n = len(s)
    list_1 = []
    list_2 = []
    for i in range(n):
        if s[i] > t[i]:
            list_1.append(i)
        elif s[i] < t[i]:
            list_2.append(i)
    x = list(s)
    for i in list_1:
        x[i] = t[i]
        res.append("".join(x))
    for i in reversed(list_2):
        x[i] = t[i]
        res.append("".join(x))
    # print(res)
    res = [str(len(res))] + res
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    for r in res:
        print(r)


def test():
    assert solve("adbe", "bcbc") == ["3", "acbe", "acbc", "bcbc"]
    assert solve("abcde", "abcde") == ["0"]
    assert solve("afwgebrw", "oarbrenq") == [
        "8",
        "aawgebrw","aargebrw", "aarbebrw", "aarbebnw",
        "aarbebnq", "aarbeenq", "aarbrenq", "oarbrenq"
    ]


if __name__ == "__main__":
    test()
    main()
