from collections import defaultdict


def solve_sub(t_left, t_right, d, h_rest):
    left = t_left
    right = t_right
    while left + 1 < right:
        mid = (left + right) // 2
        if (mid - t_left) * d * (mid + t_left + 1) // 2 >= h_rest:
            right = mid
        else:
            left = mid
    # print(right)
    return right



def solve(n, h, td_list):
    td_dict = defaultdict(int)
    for t, d in td_list:
        td_dict[t] = max(d, td_dict[t])
    t_list_s = list(sorted(list(td_dict.keys())))
    d_list_s = [td_dict[t] for t in t_list_s]
    m = len(t_list_s)
    # print(t_list_s)
    # print(d_list_s)
    # cum max
    d_max_list_s = [0] * m
    d_max_list_s[-1] = d_list_s[-1]
    for i in range(m - 2, -1, -1):
        d_max_list_s[i] = max(d_max_list_s[i + 1], d_list_s[i])
    # print(d_max_list_s)
    i = 0
    j = 1
    vt_list = []
    while j < m:
        if d_max_list_s[i] * t_list_s[i] < d_max_list_s[j] * t_list_s[j]:
            # change
            s = d_max_list_s[i] * t_list_s[i]
            t = s // d_max_list_s[j]
            vt_list.append((t_list_s[i], d_max_list_s[i], t))
            i, j = j, j + 1
        else:
            j += 1
    vt_list.append((t_list_s[i], d_max_list_s[i], 3 * 10 ** 18))
    # print(vt_list)

    h_rest = h
    t_left = 0
    for t, d, t_right in vt_list:
        # print(t_left, h_rest)
        if t <= t_left:
            s = (t_right - t_left) * d * t
            if h_rest <= s:
                return (t_left + h_rest - 1) // (d * t) + 1
        elif t_right <= t:
            s = (t_right - t_left) * d * (t_right + t_left + 1) // 2
            if h_rest <= s:
                return solve_sub(t_left, t_right, d, h_rest)
        else:
            s_1 = (t - t_left) * d * (t + t_left + 1) // 2
            if h_rest <= s_1:
                return solve_sub(t_left, t, d, h_rest)
            s_2 = (t_right - t) * d * t
            s = s_1 + s_2
            if h_rest <= s:
                return t + (h_rest - s_1 - 1) // (d * t) + 1
        h_rest -= s
        t_left = t_right
    return -1


def main():
    n, h = map(int, input().split())
    td_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, h, td_list)
    print(res)


def test():
    assert solve(2, 20, [(2, 2), (5, 1)]) == 6
    assert solve(10, 200, [
        (1, 21), (1, 1), (1, 1), (8, 4), (30, 1),
        (3, 1), (10, 2), (8, 1), (9, 1), (4, 4)
    ]) == 9


if __name__ == "__main__":
    test()
    main()
