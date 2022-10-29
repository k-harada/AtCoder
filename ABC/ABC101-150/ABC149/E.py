from bisect import bisect_left


def solve(n, m, a_list):

    a_list_s = list(sorted(a_list))
    a_list_rs_cum = []
    cum = 0
    for v in reversed(a_list_s):
        cum += v
        a_list_rs_cum.append(cum)
    # print(a_list_rs_cum)
    left = 0
    right = 2 * 10 ** 5 + 1

    while right > left + 1:
        mid = (left + right) // 2
        res_mid = 0
        for i in range(n):
            res_mid += n - bisect_left(a_list_s, mid - a_list[i])
        if res_mid >= m:
            left = mid
        else:
            right = mid
    # print(left)
    res = 0
    res_cnt = 0
    for i in range(n):
        c = n - bisect_left(a_list_s, left - a_list[i])
        if c > 0:
            res += a_list_rs_cum[c - 1] + c * a_list[i]
            res_cnt += c
            # print(i, c)

    if res_cnt > m:
        res -= left * (res_cnt - m)
    # print(res, res_cnt)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(5, 3, [10, 14, 19, 34, 33]) == 202
    assert solve(9, 14, [1, 3, 5, 110, 24, 21, 34, 5, 3]) == 1837
    assert solve(9, 73, [67597, 52981, 5828, 66249, 75177, 64141, 40773, 79105, 16076]) == 8128170


if __name__ == "__main__":
    test()
    main()
