from itertools import permutations


LARGE = 10 ** 9 + 7


def solve(n, a, m, xy_list):
    res = LARGE
    ng = [[0] * n for _ in range(n)]
    for x, y in xy_list:
        ng[x - 1][y - 1] = 1
        ng[y - 1][x - 1] = 1

    for p in permutations(range(n)):
        f = 0
        for i in range(n - 1):
            if ng[p[i]][p[i + 1]]:
                f = 1
        if f:
            continue
        r = 0
        for i in range(n):
            r += a[p[i]][i]

        res = min(r, res)

    if res == LARGE:
        return -1
    else:
        return res


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, a, m, xy_list)
    print(res)


def test():
    assert solve(3, [[1, 10, 100], [10, 1, 100], [100, 10, 1]], 1, [(1, 2)]) == 111
    assert solve(4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 3, [(1, 2), (1, 3), (2, 3)]) == -1
    assert solve(3, [[1, 10, 100], [10, 1, 100], [100, 10, 1]], 0, []) == 3


if __name__ == "__main__":
    test()
    main()
