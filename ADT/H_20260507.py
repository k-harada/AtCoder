from bisect import bisect_left, bisect_right


def solve(n, m, k, a_list):
    if n == m:
        return [0] * n
    a_list_s = list(sorted(a_list, reverse=True))
    a_list_s_ = list(sorted(a_list))
    res_list = []
    # 残り
    r = k - sum(a_list)
    # print(r)
    a_m = a_list_s[m - 1]

    # 累積和の前計算
    s_pre = []
    x = a_list_s[m - 1]
    c = 1
    s = 0
    for i in range(m - 1, -1, -1):
        s += c * (a_list_s[i] - x)
        s_pre.append(s)
        c += 1
        x = a_list_s[i]
    # print(s_pre)

    for i in range(n):
        a = a_list[i]
        if r < a_m - a:
            # 暫定m番目に追いつけない
            res_list.append(-1)
        elif a < a_m:
            r_0 = r - (a_m - a)
            j = bisect_right(s_pre, r_0)
            r_0 -= s_pre[j - 1]
            # この(j + 1)人で争う、単独最下位でなければ良い
            # print(j, r_0, (r_0 + 1) // (j + 1), a_list_s[m - j], a)
            res = (r_0 + 1) // (j + 1) + a_list_s[m - j] - a
            res_list.append(res)
        else:
            # 自分が何番目か
            jj = n - 1 - bisect_left(a_list_s_, a)
            # 暫定m + 1番目が自分に追いつくためのコスト
            r_0 = r - (a_m - a_list_s[m])
            if r_0 <= 0:
                res_list.append(0)
            else:
                j = bisect_right(s_pre, r_0)
                if (jj + 1) + (j + 1) <= m + 1:
                    res_list.append(0)
                else:
                    r_0 -= s_pre[j - 1]
                    res = (r_0 + 1) // (j + 1) + a_list_s[m - j] - a
                    res_list.append(res)
    # print(res_list)
    return res_list


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 2, 16, [3, 1, 4, 1, 5]) == [2, -1, 1, -1, 0]
    assert solve(12, 1, 570, [
        81, 62, 17, 5, 5, 86, 15, 7, 79, 26, 6, 28
    ]) == [79, 89, 111, 117, 117, 74, 112, 116, 80, 107, 117, 106]


if __name__ == "__main__":
    test()
    main()




