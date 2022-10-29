from itertools import product


def solve(n, a_list):

    res = 0

    if n == 1:
        return a_list[0][0]

    if n == 2:
        d = product(range(1, 4), range(1, 2))
    elif n == 3:
        d = product(range(1, 6), range(1, 4), range(1, 2))
    elif n == 4:
        d = product(range(1, 8), range(1, 6), range(1, 4), range(1, 2))
    elif n == 5:
        d = product(range(1, 10), range(1, 8), range(1, 6), range(1, 4), range(1, 2))
    elif n == 6:
        d = product(range(1, 12), range(1, 10), range(1, 8), range(1, 6), range(1, 4), range(1, 2))
    elif n == 7:
        d = product(range(1, 14), range(1, 12), range(1, 10), range(1, 8), range(1, 6), range(1, 4), range(1, 2))
    elif n == 8:
        d = product(range(1, 16), range(1, 14), range(1, 12), range(1, 10), range(1, 8), range(1, 6), range(1, 4), range(1, 2))

    for p in d:
        used = [0] * (2 * n)
        r = 0
        for i in range(n):
            c = 0
            for j in range(2 * n):
                if used[j] == 0:
                    if c == 0:
                        s = j
                        used[s] = 1
                    elif c == p[i]:
                        t = j
                        used[t] = 1
                        break
                    c += 1
            r = r ^ a_list[s][t - s - 1]

        res = max(res, r)

    return res


def main():
    n = int(input())
    a_list = [list(map(int, input().split())) for _ in range(2 * n - 1)]
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [[4, 0, 1], [5, 3], [2]]) == 6
    assert solve(1, [[5]]) == 5


def test_large():
    print(solve(8, [[1] * 16 for _ in range(16)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
