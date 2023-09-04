def solve_sub(n, x_list, le_list, x_base):
    rev_list = []
    d_list = []
    leg_list = []
    j = 0
    next_x = 10 ** 18 + 9
    for i in range(n):
        x = x_list[i] - x_base
        if x <= 0:
            rev_list.append(-x)
        else:
            next_x = min(next_x, x)
            if j == n:
                return 0, min(d_list), 1
            while le_list[j] < x:
                leg_list.append(le_list[j])
                d_list.append(x - le_list[j])
                j += 1
                if j == n:
                    return 0, min(d_list), 1
            j += 1
    for k in range(j, n):
        leg_list.append(le_list[k])
    if len(d_list) == 0:
        # rev_list vs leg_list
        rev_list = list(sorted(rev_list))
        r = min([x - y for x, y in zip(leg_list, rev_list)])
        if x_base >= x_list[-1]:
            if r < 0:
                return 0, 0, 0
            return r + 1, 0, 0
        else:
            if r < 0:
                return 0, next_x, 1
            return min(r + 1, next_x), next_x, 1
    else:
        d = min(d_list)
        d = min(d, next_x)
        # rev_list vs leg_list
        rev_list = list(sorted(rev_list))
        r = min([x - y for x, y in zip(leg_list, rev_list)])
        if r < 0:
            # print("a")
            return 0, d, 1
        elif r < d:
            # print("b")
            return r + 1, d, 1
        else:
            # print("c")
            return d, d, 1


def solve(n, x_list, le_list):
    res = 0
    # 左端より左
    d_min = 10 ** 18 + 1
    x_base = x_list[0]
    for i in range(n):
        d = le_list[i] - (x_list[i] - x_base)
        d_min = min(d_min, d)
    if d_min > 0:
        res += d_min
    # 左端
    x_base = x_list[0]
    while True:
        r, d, f = solve_sub(n, x_list, le_list, x_base)
        x_base += d
        res += r
        # print(r, x_base)
        if f == 0:
            break
    # print(res)
    return res


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    le_list = list(map(int, input().split()))
    res = solve(n, x_list, le_list)
    print(res)


def test():
    assert solve(3, [-6, 0, 7], [3, 5, 10]) == 6
    assert solve(1, [0], [1000000000000000000]) == 2000000000000000001
    assert solve(2, [-100, 100], [1, 1]) == 0


if __name__ == "__main__":
    test()
    main()
