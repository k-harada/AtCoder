MOD = 998244353
HALF = pow(2, MOD - 2, MOD)


def solve_sub(b, d, m):
    if b == 0 or d == 0:
        return 0
    # a = 1, c = 1
    if d % 2 == 0:
        sub_r1 = d * d // 4
        sub_r2 = d * d // 4 + (m + 1) * (d // 2)
    else:
        sub_r1 = (d + 1) * (d + 1) // 4
        sub_r2 = ((d - 1) // 2) ** 2 + (m + 1) * (d // 2)
    sub_r1 %= MOD
    sub_r2 %= MOD
    # print(sub_r1, sub_r2)
    if b % 2 == 0:
        dif = 2 * m * ((d + 1) // 2)
        dif %= MOD
        s1_times_2 = 2 * sub_r1 + ((b // 2) - 1) * dif
        s1_times_2 %= MOD
        s1_times_2 *= (b // 2)
        s1_times_2 %= MOD

        dif = 2 * m * (d // 2)
        dif %= MOD
        s2_times_2 = 2 * sub_r2 + ((b // 2) - 1) * dif
        s2_times_2 %= MOD
        s2_times_2 *= (b // 2)
        s2_times_2 %= MOD

        s_times_2 = (s1_times_2 + s2_times_2)
    else:
        dif = 2 * m * ((d + 1) // 2)
        dif %= MOD
        s1_times_2 = 2 * sub_r1 + (b // 2) * dif
        s1_times_2 %= MOD
        s1_times_2 *= (b // 2 + 1)
        s1_times_2 %= MOD

        dif = 2 * m * (d // 2)
        dif %= MOD
        s2_times_2 = 2 * sub_r2 + ((b // 2) - 1) * dif
        s2_times_2 %= MOD
        s2_times_2 *= (b // 2)
        s2_times_2 %= MOD

        s_times_2 = (s1_times_2 + s2_times_2)
    s = (s_times_2 * HALF) % MOD
    # print(s1_times_2, s2_times_2)
    # print(b, d, m, s)
    return s


def solve(n, m, q, query_list):
    res = []
    for a, b, c, d in query_list:
        r = solve_sub(b, d, m) - solve_sub(b, c - 1, m) - solve_sub(a - 1, d, m) + solve_sub(a - 1, c - 1, m)
        r %= MOD
        res.append(r)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve_sub(5, 1, 4) == 27
    assert solve_sub(5, 4, 4) == 104
    assert solve_sub(4, 4, 4) == 68
    assert solve_sub(5, 3, 4) == 80
    assert solve(5, 4, 6, [(1, 3, 2, 4), (1, 5, 1, 1), (5, 5, 1, 4), (4, 4, 2, 2), (5, 5, 4, 4), (1, 5, 1, 4)]) == [
        28, 27, 36, 14, 0, 104
    ]
    assert solve(1000000000, 1000000000, 3, [
        (1000000000, 1000000000, 1000000000, 1000000000),
        (165997482, 306594988, 719483261, 992306147),
        (1, 1000000000, 1, 1000000000)
    ]) == [
        716070898, 240994972, 536839100
    ]
    assert solve(999999999, 999999999, 3, [
        (999999999, 999999999, 999999999, 999999999),
        (216499784, 840031647, 84657913, 415448790),
        (1, 999999999, 1, 999999999)
    ]) == [
        712559605, 648737448, 540261130
    ]


if __name__ == "__main__":
    test()
    main()
