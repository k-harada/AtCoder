from bisect import bisect_right


def solve(n, d, a, xh_list):
    res = 0
    xh_list_s = sorted(xh_list, key=lambda x: x[0])
    x_list_s = [xh[0] for xh in xh_list_s]
    h_list_s = [xh[1] for xh in xh_list_s]
    dmg = 0
    wait_list = [0] * (n + 1)
    for i in range(n):
        dmg -= wait_list[i]
        v = h_list_s[i] - dmg
        if v > 0:
            t = (v - 1) // a + 1
            res += t
            dmg += t * a
            j = bisect_right(x_list_s, x_list_s[i] + 2 * d)
            wait_list[j] += t * a

    return res


def main():
    n, d, a = map(int, input().split())
    xh_list = []
    for _ in range(n):
        x, h = map(int, input().split())
        xh_list.append((x, h))
    res = solve(n, d, a, xh_list)
    print(res)


def test():
    assert solve(3, 3, 2, [(1, 2), (5, 4), (9, 2)]) == 2
    assert solve(9, 4, 1, [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 2), (7, 3), (8, 4), (9, 5)]) == 5
    assert solve(3, 0, 1, [(300000000, 1000000000), (100000000, 1000000000), (200000000, 1000000000)]) == 3000000000


if __name__ == "__main__":
    test()
    main()
