def solve_sub(m, x, y):
    # print("1:", m, x, y)
    if x % 2 == 0:
        # 1 to x - 1
        s1 = (1 + (x - 1)) * (x // 2) // 2
        # m + 2 to m + x
        s2 = ((m + 2) + (m + x)) * (x // 2) // 2
    else:
        # 1 to x
        s1 = (1 + x) * ((x + 1) // 2) // 2
        # m + 2 to m + x - 1
        s2 = ((m + 2) + (m + x - 1)) * ((x - 1) // 2) // 2
    s = s1 + s2
    # print("2:", s1, s2, s)

    if y % 2 == 0:
        # s to s + (y // 2 - 1) * x * m
        ss = (s + s + (y // 2 - 1) * x * 2 * m) * (y // 2) // 2
    else:
        ss = (s + s + (y // 2 - 1) * x * 2 * m) * (y // 2) // 2
        ss += s1 + (y - 1) * ((x + 1) // 2) * m
    return ss % 998244353


def solve(n, m, q, abcd_list):
    res = []
    for a, b, c, d in abcd_list:
        r = solve_sub(m, d, b)
        # print(b, d, r)
        if a > 1:
            # print(solve_sub(m, d, a - 1))
            r -= solve_sub(m, d, a - 1)
        if c > 1:
            # print(solve_sub(m, c - 1, b))
            r -= solve_sub(m, c - 1, b)
        if a > 1 and c > 1:
            # print(solve_sub(m, c - 1, a - 1))
            r += solve_sub(m, c - 1, a - 1)
        res.append(r % 998244353)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    q = int(input())
    abcd_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, abcd_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 4, 6, [
        (1, 3, 2, 4),
        (1, 5, 1, 1),
        (5, 5, 1, 4),
        (4, 4, 2, 2),
        (5, 5, 4, 4),
        (1, 5, 1, 4),
    ]) == [28, 27, 36, 14, 0, 104]
    assert solve(1000000000, 1000000000, 3, [
        (1000000000, 1000000000, 1000000000, 1000000000),
        (165997482, 306594988, 719483261, 992306147),
        (1, 1000000000, 1, 1000000000)
    ]) == [716070898, 240994972, 536839100]
    assert solve(999999999, 999999999, 3, [
        (999999999, 999999999, 999999999, 999999999),
        (216499784, 840031647, 84657913, 415448790),
        (1, 999999999, 1, 999999999)
    ]) == [712559605, 648737448, 540261130]


if __name__ == "__main__":
    test()
    main()
