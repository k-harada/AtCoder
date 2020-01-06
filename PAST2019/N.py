from bisect import bisect_left


def solve(n, w, c, l_list, r_list, p_list):

    p_sum = sum(p_list)

    l_list_ = [[l_list[i], i] for i in range(n)]
    l_list_s = sorted(l_list_, key=lambda x: x[0])

    left_dict = {}
    cum_left = sum(p_list)
    left_dict[0] = cum_left
    for i in range(n):
        l, j = l_list_s[i]
        if l not in left_dict.keys():
            left_dict[l] = cum_left
        cum_left -= p_list[j]
    left_dict[w] = 0

    r_list_ = [[r_list[i], i] for i in range(n)]
    r_list_s = sorted(r_list_, key=lambda x: x[0])

    right_dict = {}
    cum_right = 0
    right_dict[0] = 0
    for i in range(n):
        r, j = r_list_s[i]
        cum_right += p_list[j]
        right_dict[r] = cum_right

    left_list = list(sorted(left_dict.keys()))

    res = p_sum

    for x in right_dict.keys():
        if x + c <= w:
            d = bisect_left(left_list, x + c)
            y = left_list[d]
            cost_x = p_sum - right_dict[x] - left_dict[y]
            # print(x, y, cost_x)
            res = min(res, cost_x)

    return res


def main():
    n, w, c = map(int, input().split())
    l_list = [0] * n
    r_list = [0] * n
    p_list = [0] * n
    for i in range(n):
        l, r, p = map(int, input().split())
        l_list[i] = l
        r_list[i] = r
        p_list[i] = p
    res = solve(n, w, c, l_list, r_list, p_list)
    print(res)


def test():
    assert solve(3, 10, 5, [1, 8, 4], [3, 10, 6], [100, 123, 3]) == 3
    assert solve(3, 10, 10, [1, 8, 4], [3, 10, 6], [100, 123, 3]) == 226
    assert solve(3, 10, 1, [1, 8, 4], [3, 10, 6], [100, 123, 3]) == 0


if __name__ == "__main__":
    test()
    main()
