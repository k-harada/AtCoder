from bisect import bisect_left, bisect_right


def solve(d, l, n, c_list, query_list):
    res_list = []
    # pre-compute
    # for search first favorite
    date_dict = dict()
    for i in range(d):
        c = c_list[i]
        if c in date_dict.keys():
            date_dict[c].append(i)
        else:
            date_dict[c] = [i]
    for i in range(d, 2 * d):
        c = c_list[i - d]
        date_dict[c].append(i)

    # print(date_dict)

    # for attention
    calc_dict = dict()
    for c in date_dict.keys():
        calc_dict[c] = [[], [], []]
    for i in range(2 * d):
        c = c_list[i - d]
        if len(calc_dict[c][0]):
            i0, x, y = calc_dict[c][0][-1], calc_dict[c][1][-1], calc_dict[c][2][-1]
            calc_dict[c][0].append(i)
            calc_dict[c][1].append(x + 1)
            calc_dict[c][2].append(y + 1 + (i - i0 - 1) // l)
        else:
            calc_dict[c][0].append(i)
            calc_dict[c][1].append(1)
            calc_dict[c][2].append(1)
    # print(calc_dict)
    # query
    for i in range(n):
        k, f, t = query_list[i]
        res = 0
        total = 0
        if k not in date_dict.keys():
            res_list.append(0)
        else:
            first_fav = date_dict[k][bisect_left(date_dict[k], (f - 1) % d)]
            if first_fav == f - 1:
                total = 0
            else:
                total += max(0, (first_fav - 1 - ((f - 1) % d)) // l) + 1
            # print(first_fav, total)
            if total >= t:
                res_list.append(0)
            else:
                # one loop
                i0 = calc_dict[k][0][0]
                ind_loop = bisect_left(calc_dict[k][0], i0 + d)
                total_one = calc_dict[k][2][ind_loop] - 1
                fav_one = calc_dict[k][1][ind_loop] - 1
                # print(k, fav_one, total_one)
                # add loop
                n_loop = (t - total) // total_one
                res += n_loop * fav_one
                total += n_loop * total_one
                # print(res, total)
                if total == t:
                    res_list.append(res)
                else:
                    # rest
                    to_add = t - total
                    first_fav_ind = bisect_left(calc_dict[k][0], first_fav)
                    target_total = calc_dict[k][2][first_fav_ind] + to_add - 1
                    target_ind = bisect_right(calc_dict[k][2], target_total) - 1
                    res += calc_dict[k][1][target_ind] - calc_dict[k][1][first_fav_ind] + 1
                    res_list.append(res)

    return res_list


def main():
    d, l, n = map(int, input().split())
    c_list = list(map(int, input().split()))
    query_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(d, l, n, c_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 2, 3, [2, 3, 1, 3], [[1, 2, 2], [3, 3, 1], [3, 4, 3]]) == [1, 0, 3]
    assert solve(3, 1, 3, [1, 1, 1], [[2, 1, 3], [1, 2, 3], [1, 3, 3]]) == [0, 3, 3]
    # print(solve(10, 4, 4, [4, 4, 4, 3, 1, 1, 5, 2, 2, 1], [[2, 5, 2], [2, 9, 10], [2, 3, 3], [2, 7, 13]]))
    assert solve(10, 4, 4, [4, 4, 4, 3, 1, 1, 5, 2, 2, 1], [[2, 5, 2], [2, 9, 10], [2, 3, 3], [2, 7, 13]]) == [1, 5, 1, 6]


if __name__ == "__main__":
    test()
    main()
