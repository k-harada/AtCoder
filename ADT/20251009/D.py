def solve(s, t):
    false_list = []
    for i in range(len(s)):
        if s[i] != t[i]:
            false_list.append(i)
    if len(false_list) == 0:
        return "Yes"
    elif len(false_list) == 2:
        i, j = false_list
        if i + 1 != j:
            return "No"
        elif s[i] != t[j] or s[j] != t[i]:
            return "No"
        else:
            return "Yes"
    else:
        return "No"


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("abc", "acb") == "Yes"
    assert solve("aabb", "bbaa") == "No"
    assert solve("abcde", "abcde") == "Yes"


if __name__ == "__main__":
    test()
    main()
