def solve(n, c, abc_list):
    # diff dict
    cost_diff_dict = dict()
    for a, b, cost in abc_list:
        if a - 1 not in cost_diff_dict.keys():
            cost_diff_dict[a - 1] = cost
        else:
            cost_diff_dict[a - 1] += cost
        if b not in cost_diff_dict.keys():
            cost_diff_dict[b] = -cost
        else:
            cost_diff_dict[b] -= cost

    t_list = list(sorted(cost_diff_dict.keys()))
    m = len(t_list)
    # print(t_list)
    res = 0
    cost_now = 0
    for i in range(m - 1):
        t = t_list[i]
        cost_now += cost_diff_dict[t]
        res += min(cost_now, c) * (t_list[i + 1] - t)

    return res


def main():
    n, c = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, c, abc_list)
    print(res)


def test():
    assert solve(2, 6, [(1, 2, 4), (2, 2, 4)]) == 10
    assert solve(5, 1000000000, [
        (583563238, 820642330, 44577),
        (136809000, 653199778, 90962),
        (54601291, 785892285, 50554),
        (5797762, 453599267, 65697),
        (468677897, 916692569, 87409)
    ]) == 163089627821228
    assert solve(5, 100000, [
        (583563238, 820642330, 44577),
        (136809000, 653199778, 90962),
        (54601291, 785892285, 50554),
        (5797762, 453599267, 65697),
        (468677897, 916692569, 87409)
    ]) == 88206004785464


if __name__ == "__main__":
    test()
    main()
