def solve(n, m, a_list):
    b_list = list(range(n + 1))
    switch_list = []
    for a in a_list:
        b_list[a], b_list[a + 1] = b_list[a + 1], b_list[a]
        switch_list.append((b_list[a], b_list[a + 1]))
    res_list = []
    res_rev = [0] * (n + 1)
    for i, b in enumerate(b_list):
        res_rev[b] = i
    for s, t in switch_list:
        s, t = min(s, t), max(s, t)
        if s != 1:
            res_list.append(res_rev[1])
        else:
            res_list.append(res_rev[t])
    return res_list


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 4, [1, 2, 3, 2]) == [1, 3, 2, 4]
    assert solve(3, 3, [2, 2, 2]) == [1, 1, 1]
    assert solve(10, 10, [1, 1, 1, 9, 4, 4, 2, 1, 3, 3]) == [2, 2, 2, 3, 3, 3, 1, 3, 4, 4]


if __name__ == "__main__":
    test()
    main()
