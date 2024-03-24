def solve(n, a, b, s):
    cnt_left = 0
    cnt_right = 0
    for c in s:
        if c == "(":
            cnt_left += 1
        else:
            cnt_right += 1
    res = 0
    s_list = list(s)
    if cnt_left > cnt_right:
        cnt = (cnt_left - cnt_right) // 2
        res += b * cnt
        for i in range(2 * n - 1, -1, -1):
            if s_list[i] == "(" and cnt > 0:
                s_list[i] = ")"
                cnt -= 1
    elif cnt_left < cnt_right:
        cnt = (cnt_right - cnt_left) // 2
        res += b * cnt
        for i in range(2 * n):
            if s_list[i] == ")" and cnt > 0:
                s_list[i] = "("
                cnt -= 1
    # print(s_list)
    # print(res)
    cnt_total = [0]
    for c in s_list:
        if c == "(":
            cnt_total.append(cnt_total[-1] + 1)
        else:
            cnt_total.append(cnt_total[-1] - 1)
    cnt_min = (-1) * min(cnt_total)
    # print(cnt_min)
    if cnt_min > 0:
        res += min(a, 2 * b) * ((cnt_min + 1) // 2)
    # print(res)
    return res


def main():
    n, a, b = map(int, input().split())
    s = input()
    res = solve(n, a, b, s)
    print(res)


def test():
    assert solve(3, 3, 2, ")))(()") == 5
    assert solve(1, 175, 1000000000, "()") == 0
    assert solve(7, 2622, 26092458, "))()((((()()((") == 52187538


if __name__ == "__main__":
    test()
    main()
