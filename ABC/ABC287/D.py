def solve(s, t):
    m = len(t)
    front = [0] * (m + 1)
    front[0] = 1
    for i in range(m):
        if s[i] == t[i] or s[i] == "?" or t[i] == "?":
            front[i + 1] = 1
        else:
            break
    back = [0] * (m + 1)
    back[0] = 1
    for i in range(1, m + 1):
        if s[-i] == t[-i] or s[-i] == "?" or t[-i] == "?":
            back[i] = 1
        else:
            break
    res = []
    for i in range(m + 1):
        if front[i] * back[m - i] == 1:
            res.append("Yes")
        else:
            res.append("No")
    # print(res)
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    for r in res:
        print(r)


def test():
    assert solve("a?c", "b?") == ["Yes", "No", "No"]
    assert solve("atcoder", "?????") == ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
    assert solve("beginner", "contest") == ["No", "No", "No", "No", "No", "No", "No", "No"]


if __name__ == "__main__":
    test()
    main()
