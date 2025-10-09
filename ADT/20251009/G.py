def solve_sub(n, sub_list):
    if len(sub_list) == 0:
        return 0
    res = 2
    c_list = dict()
    for a in sub_list:
        c_list[a] = 0
    left = 0
    right = 0
    m = len(sub_list)
    c_list[sub_list[right]] = 1
    while right < m:
        if c_list[sub_list[right]] == 2:
            c_list[sub_list[left]] -= 1
            left += 1
            if c_list[sub_list[right]] == 1:
                res = max(res, (right - left + 1) * 2)
                # print(left, right, c_list)
        elif right < m - 1:
            right += 1
            c_list[sub_list[right]] += 1
            if c_list[sub_list[right]] == 1:
                res = max(res, (right - left + 1) * 2)
                # print(left, right, c_list)
        else:
            break

    return res


def solve(n, a_list):
    # print(a_list)
    sub_list_list = []
    sub_list = []
    i = 0
    while i + 1 < n:
        # print(i)
        if a_list[i] == a_list[i + 1]:
            sub_list.append(a_list[i])
        else:
            if len(sub_list):
                sub_list_list.append(sub_list)
            sub_list = []
        i += 2
    if len(sub_list):
        sub_list_list.append(sub_list)
    sub_list = []
    i = 1
    while i + 1 < n:
        # print(i)
        if a_list[i] == a_list[i + 1]:
            sub_list.append(a_list[i])
        else:
            if len(sub_list):
                sub_list_list.append(sub_list)
            sub_list = []
        i += 2
    if len(sub_list):
        sub_list_list.append(sub_list)
    # print(sub_list_list)
    res = 0
    for sub_list in sub_list_list:
        # print(sub_list, solve_sub(n, sub_list))
        res = max(res, solve_sub(n, sub_list))
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(8, [2, 3, 1, 1, 2, 2, 1, 1]) == 4
    assert solve(3, [1, 2, 2]) == 2
    assert solve(1, [1]) == 0


if __name__ == "__main__":
    test()
    main()
