from bisect import bisect_left


def solve(h, w, r_s, c_s, n, rc_list, q, dl_list):
    # 壁の処理
    lr_dict = dict()
    ud_dict = dict()
    rc_list_s = list(sorted(rc_list, key=lambda x: (x[0], x[1])))
    for r, c in rc_list_s:
        if r in lr_dict.keys():
            lr_dict[r].append(c)
        else:
            lr_dict[r] = [c]
    rc_list_s = list(sorted(rc_list, key=lambda x: (x[1], x[0])))
    for r, c in rc_list_s:
        if c in ud_dict.keys():
            ud_dict[c].append(r)
        else:
            ud_dict[c] = [r]

    res = []
    r, c = r_s, c_s
    for d, l_str in dl_list:
        l_int = int(l_str)
        if d == "L":
            if r in lr_dict.keys():
                i = bisect_left(lr_dict[r], c)
                if i > 0:
                    c = max(lr_dict[r][i - 1] + 1, c - l_int)
                else:
                    c = max(1, c - l_int)
            else:
                c = max(1, c - l_int)
        elif d == "R":
            if r in lr_dict.keys():
                i = bisect_left(lr_dict[r], c)
                if i < len(lr_dict[r]):
                    c = min(lr_dict[r][i] - 1, c + l_int)
                else:
                    c = min(w, c + l_int)
            else:
                c = min(w, c + l_int)
        elif d == "U":
            if c in ud_dict.keys():
                i = bisect_left(ud_dict[c], r)
                if i > 0:
                    r = max(ud_dict[c][i - 1] + 1, r - l_int)
                else:
                    r = max(1, r - l_int)
            else:
                r = max(1, r - l_int)
        elif d == "D":
            if c in ud_dict.keys():
                i = bisect_left(ud_dict[c], r)
                if i < len(ud_dict[c]):
                    r = min(ud_dict[c][i] - 1, r + l_int)
                else:
                    r = min(h, r + l_int)
            else:
                r = min(h, r + l_int)
        res.append((r, c))
    # print(res)
    return res


def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    rc_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    dl_list = [tuple(input().split()) for _ in range(q)]
    res = solve(h, w, r_s, c_s, n, rc_list, q, dl_list)
    for r in res:
        print(" ".join([str(a) for a in r]))


def test():
    assert solve(5, 5, 4, 4, 3, [(5, 3), (2, 2), (1, 4)], 4, [("L", "2"), ("U", "3"), ("L", "2"), ("R", "4")]) == [
        (4, 2), (3, 2), (3, 1), (3, 5)
    ]


def test_large():
    print(solve(10 ** 9, 10 ** 9, 10 ** 8 + 9, 1, 200000, [(i * 5000 + 1, 1) for i in range(200000)],
                200000, [("U", "1"), ("D", "1")] * 100000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
