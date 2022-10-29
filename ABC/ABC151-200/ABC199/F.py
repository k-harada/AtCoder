import numpy as np


MOD = 10 ** 9 + 7


# function to avoid overflow
# (10 ** 9) ^ 2 * 100 is dangerous
def matmul_mod(a, b, mod, d):
    res = np.matmul(a, b // d) % mod
    res *= d
    res %= mod
    res += np.matmul(a, b % d) % mod
    res %= mod
    return res


def solve(n, m, k, a_list, xy_list):
    r = np.array(a_list).reshape((n, 1))
    g = 2 * m * np.identity(n, dtype=int)
    for x, y in xy_list:
        g[x - 1, y - 1] += 1
        g[y - 1, x - 1] += 1
        g[x - 1, x - 1] -= 1
        g[y - 1, y - 1] -= 1

    g *= pow(2 * m, MOD - 2, MOD)
    g %= MOD

    while k > 0:
        if k % 2 == 1:
            r = matmul_mod(g, r, MOD, 10000)
        g = matmul_mod(g, g, MOD, 10000)
        k = k // 2

    return [x[0] for x in r]


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res_list = solve(n, m, k, a_list, xy_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, 2, 1, [3, 1, 5], [(1, 2), (1, 3)]) == [3, 500000005, 500000008]
    assert solve(3, 2, 2, [12, 48, 36], [(1, 2), (1, 3)]) == [750000036, 36, 250000031]
    assert solve(4, 5, 1000, [578, 173, 489, 910], [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]) == [
        201113830, 45921509, 67803140, 685163678
    ]


if __name__ == "__main__":
    test()
    main()
