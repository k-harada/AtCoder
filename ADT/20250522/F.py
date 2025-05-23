import itertools


def solve(c):
    res = 0
    line_list = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for p in itertools.permutations(list(range(9))):
        x = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        r = 0
        for i in p:
            x[i] = c[i // 3][i % 3]
            for a_, b_, c_ in line_list:
                if i not in [a_, b_, c_]:
                    continue
                aa, bb, cc = x[a_], x[b_], x[c_]
                if max([aa, bb, cc]) > 0 > aa * bb * cc and len({aa, bb, cc}) == 2:
                    r = 1
        res += r
    res = res / (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
    # print(res)
    return 1 - res


def main():
    c = [tuple(map(int, input().split())) for _ in range(3)]
    res = solve(c)
    print(res)


def test():
    assert abs(solve([(3, 1, 9), (2, 5, 6), (2, 7, 1)]) - 2 / 3) < 10 ** (-9)
    assert abs(solve([(7, 7, 6), (8, 6, 8), (7, 7, 6)]) - 0.004982363315696649029982363316) < 10 ** (-9)
    assert abs(solve([(3, 6, 7), (1, 9, 7), (5, 7, 5)]) - 0.4) < 10 ** (-9)


if __name__ == "__main__":
    # test()
    main()
