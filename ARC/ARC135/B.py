def solve(n, s_list):
    # a1 = 0とする
    # a1, a4, a7, ...
    a1_list = [0]
    for i in range(1, n, 3):
        a1_list.append(a1_list[-1] + s_list[i] - s_list[i - 1])
    m1 = min(a1_list)
    a1_list_p = [a - m1 for a in a1_list]
    # a2 = 0とする
    # a2, a5, a8, ...
    a2_list = [0]
    for i in range(2, n, 3):
        a2_list.append(a2_list[-1] + s_list[i] - s_list[i - 1])
    m2 = min(a2_list)
    a2_list_p = [a - m2 for a in a2_list]
    # a3 = 0とする
    # a3, a6, a9, ...
    a3_list = [0]
    for i in range(3, n, 3):
        a3_list.append(a3_list[-1] + s_list[i] - s_list[i - 1])
    m3 = min(a3_list)
    a3_list_p = [a - m3 for a in a3_list]

    if a1_list_p[0] + a2_list_p[0] + a3_list_p[0] > s_list[0]:
        return ["No"]
    d = s_list[0] - (a1_list_p[0] + a2_list_p[0] + a3_list_p[0])
    a1_list_p = [d + a for a in a1_list_p]
    # print(a1_list_p)
    # print(a2_list_p)
    # print(a3_list_p)
    res = []
    for i in range(n + 2):
        if i % 3 == 0:
            res.append(a1_list_p[i // 3])
        elif i % 3 == 1:
            res.append(a2_list_p[i // 3])
        else:
            res.append(a3_list_p[i // 3])
    return ["Yes", " ".join([str(r) for r in res])]


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [6, 9, 6, 6, 5]) == ["Yes", "3 3 0 6 0 0 5"]
    assert solve(5, [0, 1, 2, 1, 0]) == ["No"]
    assert solve(1, [10]) == ["Yes", "10 0 0"]


if __name__ == "__main__":
    test()
    main()
