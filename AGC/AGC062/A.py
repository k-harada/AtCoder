def solve_sub(n, s):
    if s[-1] == "A":
        return "A"
    c = 0
    for i in range(n - 1):
        if s[i] == "B" and s[i + 1] == "A":
            c += 1
    if c == 0:
        return "B"
    else:
        return "A"


def solve(t, ns_list):
    res = []
    for n, s in ns_list:
        res.append(solve_sub(n, s))
    return res


def solve_greed(s):
    a_list = []
    b_list = []
    for i, c in enumerate(s[:-1]):
        if c == "A":
            a_list.append(i)
        else:
            b_list.append(i)
    res = ""
    for i in a_list:
        res = res + s[i + 1]
    for i in b_list:
        res = res + s[i + 1]
    return res


def main():
    t = int(input())
    ns_list = []
    for _ in range(t):
        n = int(input())
        s = input()
        ns_list.append((n, s))
    res = solve(t, ns_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(2, "AB"), (3, "AAA"), (4, "ABAB")]) == ["B", "A", "A"]


def test_2():
    s = input()
    print(solve_greed(s))
    # print(solve_sub(s))


if __name__ == "__main__":
    test()
    main()
