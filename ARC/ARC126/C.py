import math
from bisect import bisect_left, bisect_right


def solve(n, k, a_list):
    rt = int(math.sqrt(300000))
    a_list_s = list(sorted(a_list))
    r_list = [0] * 300001
    # small
    # for m in range(1, rt):
    #     r_list[m] = sum([(-a) % m for a in a_list_s])
    a_list_s_cum = [0]
    s = 0
    for a in a_list_s:
        s += a
        a_list_s_cum.append(s)

    # large
    for m in range(1, 300001):
        v = 0
        a = 0
        r = 0
        while v <= 300000:
            v += m
            b = bisect_right(a_list_s, v)
            r += (b - a) * v - (a_list_s_cum[b] - a_list_s_cum[a])
            # if v == m and m == 2400:
            #     print(a, b, a_list_s_cum[b] - a_list_s_cum[a])
            # if v == 2 * m and m == 2400:
            #     print(a, b, a_list_s_cum[b] - a_list_s_cum[a])
            a = b
        r_list[m] = r
    # print(r_list[:10])
    # print(r_list[2470:2480])
    res = 1
    for i in range(300001):
        if r_list[i] <= k:
            res = i

    # corner that k is too large
    if r_list[300000] <= k:
        res = 300000 + (k - r_list[300000]) // n
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 6, [3, 4, 9]) == 5
    assert solve(3, 4, [30, 10, 20]) == 10
    assert solve(5, 12345, [1, 2, 3, 4, 5]) == 2472


def test_large():
    print(solve(300000, 1, list(range(1, 300001))))


if __name__ == "__main__":
    # test()
    # test_large()
    main()
