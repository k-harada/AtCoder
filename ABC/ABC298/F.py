def solve(n, rcx_list):
    # 交差を無視して上からn + 1個を評価すればいい
    r_dict = dict()
    c_dict = dict()
    rc_dict = dict()
    for r, c, x in rcx_list:
        r_dict[r] = 0
        c_dict[c] = 0
        rc_dict[f"{r}_{c}"] = x
    for r, c, x in rcx_list:
        r_dict[r] += x
        c_dict[c] += x
    # 候補探索
    rv_list = []
    for r in r_dict.keys():
        rv_list.append((r, r_dict[r]))
    rv_list = list(sorted(rv_list, key=lambda rv: -rv[1]))
    cv_list = []
    for c in c_dict.keys():
        cv_list.append((c, c_dict[c]))
    cv_list = list(sorted(cv_list, key=lambda cv: -cv[1]))

    res = 0

    for r, v1 in rv_list:
        for c, v2 in cv_list:
            if f"{r}_{c}" in rc_dict.keys():
                res = max(res, v1 + v2 - rc_dict[f"{r}_{c}"])
            else:
                res = max(res, v1 + v2)
                break

    return res


def main():
    n = int(input())
    rcx_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, rcx_list)
    print(res)


def test():
    assert solve(4, [(1, 1, 2), (1, 2, 9), (2, 1, 8), (3, 2, 3)]) == 20
    assert solve(1, [(1, 1000000000, 1)]) == 1


if __name__ == "__main__":
    test()
    main()
