def solve_sub_wa(n, k, s):
    # find 1
    left_1 = n
    right_1 = -1
    for i, c in enumerate(s):
        if c == "1":
            left_1 = min(left_1, i)
            right_1 = i
    # no 1
    if left_1 == n:
        count_list = []
        r = 0
        for i, c in enumerate(s):
            if c == "?":
                r += 1
            else:
                count_list.append(r)
                r = 0
        count_list.append(r)
        if count_list.count(k) == 1 and max(count_list) == k:
            return "Yes"
        else:
            return "No"
    # 1の間に0があったら不可
    for i in range(left_1, right_1):
        if s[i] == "0":
            return "No"
    # 左側にある0
    left_0 = -1
    for i in range(left_1, -1, -1):
        if s[i] == "0":
            left_0 = i
            break
    # 右側にある0
    right_0 = n
    for i in range(right_1, n):
        if s[i] == "0":
            right_0 = i
            break
    # print(left_1, right_1, left_0, right_0)
    # そもそも長さが足りない
    if right_0 - left_0 - 1 < k:
        return "No"
    elif right_0 - left_0 - 1 == k:
        return "Yes"

    # そもそも1だけで長い
    if right_1 - left_1 + 1 > k:
        return "No"
    elif right_1 - left_1 + 1 == k:
        return "Yes"

    # 両端が?だったらだめ
    if s[right_0 - 1] == "?" and s[left_0 + 1] == "?":
        return "No"
    else:
        return "Yes"


def solve_sub(n, k, s):
    count = 0
    count_1 = 0
    count_0 = 0
    m = s.count("1")
    for i in range(k):
        if s[i] == "0":
            count_0 += 1
        elif s[i] == "1":
            count_1 += 1
    if count_0 == 0 and count_1 == m:
        count += 1

    for i in range(n - k):
        if s[k + i] == "0":
            count_0 += 1
        elif s[k + i] == "1":
            count_1 += 1
        if s[i] == "0":
            count_0 -= 1
        elif s[i] == "1":
            count_1 -= 1
        if count_0 == 0 and count_1 == m:
            count += 1

    if count == 1:
        return "Yes"
    else:
        return "No"


def solve(t, case_list):
    res = []
    for n, k, s in case_list:
        res.append(solve_sub_wa(n, k, s))
    # print(res)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        case_list.append((n, k, s))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [(3, 2, "1??"), (4, 2, "?1?0"), (6, 3, "011?1?"), (10, 5, "00?1???10?")]) == [
        "Yes", "No", "No", "Yes"
    ]


def test_random():
    import numpy as np
    for case in range(1000):
        print(case)
        n = 10
        s_list = []
        for i in range(n):
            x = np.random.choice(3)
            if x == 0:
                s_list.append("0")
            elif x == 1:
                s_list.append("1")
            else:
                s_list.append("?")
        s = "".join(s_list)
        print(s)
        for k in range(1, n):
            if solve_sub(n, k, s) != solve_sub_wa(n, k, s):
                print(n, k, s)
                print(solve_sub(n, k, s))
                print(solve_sub_wa(n, k, s))
            assert solve_sub(n, k, s) == solve_sub_wa(n, k, s)


if __name__ == "__main__":
    test()
    # test_random()
    main()
