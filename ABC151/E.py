LARGE = 10 ** 9 + 7


def solve(n, k, a_list):

    # nCk
    nck_list = [0] * (n + 1)
    nck_list[k] = 1
    for i in range(k + 1, n + 1):
        nck_list[i] = (nck_list[i - 1] * i * pow(i - k, LARGE - 2, LARGE)) % LARGE

    # value_counts
    a_cnt_dict = dict()
    for i in range(n):
        a = a_list[i]
        if a not in a_cnt_dict.keys():
            a_cnt_dict[a] = 1
        else:
            a_cnt_dict[a] += 1

    a_list_unique = list(sorted(list(a_cnt_dict.keys())))
    m = len(a_list_unique)
    a_values_cum = [0] * m
    s = 0
    for i in range(m):
        s += a_cnt_dict[a_list_unique[i]]
        a_values_cum[i] = s

    a_list_unique_rev = list(reversed(a_list_unique))
    a_values_cum_rev = [0] * m
    s = 0
    for i in range(m):
        s += a_cnt_dict[a_list_unique_rev[i]]
        a_values_cum_rev[i] = s

    # max
    s_max = 0
    d_max = 0
    for i in range(m):
        c_max = (nck_list[a_values_cum[i]] - d_max) % LARGE
        s_max += a_list_unique[i] * c_max
        s_max %= LARGE
        d_max += c_max
        d_max %= LARGE

    # min
    s_min = 0
    d_min = 0
    for i in range(m):
        c_min = (nck_list[a_values_cum_rev[i]] - d_min) % LARGE
        s_min += a_list_unique_rev[i] * c_min
        s_min %= LARGE
        d_min += c_min
        d_min %= LARGE
    # print(s_max, s_min)
    return (s_max - s_min) % LARGE


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(4, 2, [1, 1, 3, 4]) == 11
    assert solve(6, 3, [10, 10, 10, -10, -10, -10]) == 360
    assert solve(3, 1, [1, 1, 1]) == 0
    assert solve(10, 6, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0, 0, 0, 0, 0]) == 999998537


if __name__ == "__main__":
    test()
    main()
