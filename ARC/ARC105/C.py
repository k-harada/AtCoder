from itertools import permutations


def solve(n, m, w_list, lv_list):

    min_v = min([lv[1] for lv in lv_list])
    max_w = max(w_list)
    if max_w > min_v:
        return -1

    w_dict = dict()

    # pow
    for i in range(1, 2 ** n):
        w = 0
        for j in range(n):
            if i & (2 ** j):
                w += w_list[j]
        w_dict[w] = 0

    # max_len
    for l, v in lv_list:
        for w in w_dict.keys():
            if v < w:
                w_dict[w] = max(w_dict[w], l)

    res = 10 ** 9
    for p in permutations(range(n), n):
        d_list = [0]
        for i in range(1, n):
            w = w_list[p[i]]
            d = 0
            for j in range(i - 1, -1, -1):
                w += w_list[p[j]]
                d = max(d, d_list[j] + w_dict[w])
            d_list.append(d)
        res = min(res, d_list[-1])

    return res


def main():
    n, m = map(int, input().split())
    w_list = list(map(int, input().split()))
    lv_list = [list(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, w_list, lv_list)
    print(res)


def test():
    assert solve(3, 2, [1, 4, 2], [[10, 4], [2, 6]]) == 10
    assert solve(2, 1, [12, 345], [[1, 1]]) == -1
    assert solve(8, 1, [1, 1, 1, 1, 1, 1, 1, 1], [[100000000, 1]]) == 700000000


if __name__ == "__main__":
    test()
    main()
