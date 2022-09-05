def solve(n, p_list_org):
    p_list = p_list_org.copy()
    res = 0
    res_list = []

    start_left = 0
    for i in range(0, n, 2):
        if p_list[i] % 2 == 0:
            # 左に持ってくる
            for j in range(i, start_left, -2):
                p_list[j], p_list[j - 2] = p_list[j - 2], p_list[j]
                res += 1
                res_list.append(f"B {j - 1}")
            start_left += 2
    start_right = 1
    for i in range(1, n, 2):
        if p_list[i] % 2 == 1:
            # 左に持ってくる
            for j in range(i, start_right, -2):
                p_list[j], p_list[j - 2] = p_list[j - 2], p_list[j]
                res += 1
                res_list.append(f"B {j - 1}")
            start_right += 2

    # print(res)
    # print(res_list)
    # print(p_list)

    # 偶奇を直す
    for i in range(0, start_left, 2):
        p_list[i], p_list[i + 1] = p_list[i + 1], p_list[i]
        res += 1
        res_list.append(f"A {i + 1}")
    # print(res)
    # print(res_list)
    # print(p_list)

    # それぞれソートする
    while True:
        c = 0
        for i in range(0, n - 2):
            if p_list[i] > p_list[i + 2]:
                res += 1
                c += 1
                p_list[i], p_list[i + 2] = p_list[i + 2], p_list[i]
                res_list.append(f"B {i + 1}")
        if c == 0:
            break
    # print(res)
    # print(res_list)
    # print(p_list)
    return res, res_list


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res, res_list = solve(n, p_list)
    print(res)
    for r in res_list:
        print(r)


def test():
    assert solve(4, [3, 2, 4, 1]) == (4, ['B 1', 'B 2', 'A 1', 'B 2'])
    assert solve(3, [1, 2, 3]) == (0, [])
    assert solve(6, [2, 1, 4, 3, 6, 5]) == (3, ['A 1', 'A 3', 'A 5'])


if __name__ == "__main__":
    test()
    main()
