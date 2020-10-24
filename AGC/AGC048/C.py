def solve_right(n, a_list, b_list, right):

    if b_list[-1] != right:
        return -1

    a_list_ = a_list + [right + 1]
    base_ind = 0
    res = 0
    ind = 0
    for stop_ind in range(n + 1):
        while ind < n:
            if a_list_[stop_ind] - (stop_ind - ind) == b_list[ind]:
                ind += 1
            elif a_list_[stop_ind] - (stop_ind - ind) > b_list[ind]:
                return -1
            else:
                break
        if ind > base_ind:
            res += stop_ind - base_ind
            base_ind = ind
    return res


def solve(n, ll, a_list, b_list):

    solve_seq = []
    direction = "none"
    temp = []
    for i in range(n):
        if a_list[i] > b_list[i]:
            if direction == "right":
                solve_seq.append([temp, direction])
                temp = []
            direction = "left"
            temp.append(i)
        elif a_list[i] == b_list[i]:
            solve_seq.append([temp, direction])
            temp = []
            direction = "none"
        elif a_list[i] < b_list[i]:
            if direction == "left":
                solve_seq.append([temp, direction])
                temp = []
            direction = "right"
            temp.append(i)
    if direction != "none":
        solve_seq.append([temp, direction])
    # print(solve_seq)
    res = 0
    for ind_list, direction in solve_seq:
        if direction == "right":
            if ind_list[-1] < n - 1:
                if a_list[ind_list[-1] + 1] != b_list[ind_list[-1] + 1]:
                    return -1
                right = a_list[ind_list[-1] + 1] - 1
            else:
                right = ll
            m = len(ind_list)
            a_list_sub = [a_list[i] for i in ind_list]
            b_list_sub = [b_list[i] for i in ind_list]
            r = solve_right(m, a_list_sub, b_list_sub, right)
            # print("right", m, a_list_sub, b_list_sub, right, r)
            if r == -1:
                return -1
            else:
                res += r
        if direction == "left":
            if ind_list[0] > 0:
                if a_list[ind_list[0] - 1] != b_list[ind_list[0] - 1]:
                    return -1
                right = - (a_list[ind_list[0] - 1] - 1)
            else:
                right = -1
            m = len(ind_list)
            a_list_sub = [-a_list[i] for i in reversed(ind_list)]
            b_list_sub = [-b_list[i] for i in reversed(ind_list)]
            r = solve_right(m, a_list_sub, b_list_sub, right)
            # print("left", m, a_list_sub, b_list_sub, right, r)
            if r == -1:
                return -1
            else:
                res += r
        # print(ind_list, direction, res)
    return res


def main():
    n, ll = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, ll, a_list, b_list)
    print(res)


def test():
    assert solve(4, 11, [3, 4, 6, 10], [1, 5, 6, 11]) == 3
    assert solve(1, 3, [1], [2]) == -1
    assert solve(10, 1000000000, [
        65110170, 68805223, 123016442, 275946481, 661490312, 760727752, 764540566, 929355340, 930658577, 947099792
    ], [
        1, 2, 123016442, 661490311, 929355337, 930658574, 999999997, 999999998, 999999999, 1000000000
    ]) == 13


if __name__ == "__main__":
    test()
    main()
