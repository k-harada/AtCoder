def solve_sub(n):
    if n < 7:
        return -1
    r = 0
    d0 = 1
    while d0 * 2 + r <= n - 3:
        d0 *= 2
    r += d0
    d1 = 1
    while d1 * 2 + r <= n - 1 and d1 * 2 < d0:
        d1 *= 2
    r += d1
    d2 = 1
    while d2 * 2 + r <= n and d2 * 2 < d1:
        d2 *= 2
    r += d2
    # print(d0, d1, d2)
    return r


def solve(t, n_list):
    # print([solve_sub(n) for n in n_list])
    return [solve_sub(n) for n in n_list]


def main():
    t = int(input())
    n_list = [int(input()) for _ in range(t)]
    res = solve(t, n_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [16, 161, 4, 1000000000000000000]) == [14, 161, -1, 936748722493063168]


if __name__ == "__main__":
    test()
    main()
