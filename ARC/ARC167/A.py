def solve(n, m, a_list):
    b_list = [0] * m
    a_list_s = list(sorted(a_list, reverse=True))
    for i in range(m):
        b_list[i] += a_list_s[i]
    for i in range(m, n):
        b_list[-(i - m + 1)] += a_list_s[i]
    res = sum([b ** 2 for b in b_list])
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(5, 3, [1, 1, 1, 6, 7]) == 102
    assert solve(2, 1, [167, 924]) == 1190281
    assert solve(12, 9, [
        22847, 98332, 854, 68844, 81080, 46058, 40949, 62493, 76561, 52907, 88628, 99740
    ]) == 61968950639


if __name__ == "__main__":
    test()
    main()
