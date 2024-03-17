from heapq import heappop, heappush
from bisect import bisect_left


def solve(t, n_list):
    borders = [2, 14]
    while True:
        borders.append(borders[-1] * 2)
        borders.append(borders[-1] * 7)
        if borders[-1] > 10 ** 16:
            break
    res = []
    for n in n_list:
        i = bisect_left(borders, n)
        if i % 2 == 0:
            res.append("ryota")
        else:
            res.append("sepa")
    return res


def solve_tle(t, n_list):
    reduce_dict = {
        2: -1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1,
        10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: -1
    }
    h = []
    for n in n_list:
        heappush(h, -n)
    while len(h):
        p = heappop(h)
        p *= -1
        if p in reduce_dict.keys():
            continue
        else:
            reduce_dict[p] = 0
        for d in [2, 3, 5, 7]:
            q = (p + d - 1) // d
            if q in reduce_dict.keys():
                continue
            else:
                heappush(h, -q)
    # print(len(reduce_dict))
    for p in sorted(reduce_dict.keys()):
        if reduce_dict[p] != 0:
            continue
        r = -1
        for d in [2, 3, 5, 7]:
            q = (p + d - 1) // d
            if reduce_dict[q] == -1:
                r = 1
        reduce_dict[p] = r
    # for p in sorted(reduce_dict.keys()):
    #     print(p, reduce_dict[p])
    res = []
    for n in n_list:
        if reduce_dict[n] == 1:
            res.append("sepa")
        else:
            res.append("ryota")
    return res


def main():
    t = int(input())
    n_list = [int(input()) for _ in range(t)]
    res = solve(t, n_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [11, 2, 2357]) == ["sepa", "ryota", "sepa"]
    # print([(i + 2, r) for i, r in enumerate(solve(10000, [i + 2 for i in range(10000)]))])


if __name__ == "__main__":
    test()
    main()
