from itertools import permutations


def solve(n, k, t_list):

    res = 0

    for p in permutations(range(1, n)):
        d = t_list[0][p[0]]
        d += t_list[p[-1]][0]
        for i in range(n - 2):
            d += t_list[p[i]][p[i + 1]]
        if d == k:
            res += 1

    return res


def main():
    n, k = map(int, input().split())
    t_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, k, t_list)
    print(res)


def test():
    assert solve(4, 330, [[0, 1, 10, 100], [1, 0, 20, 200], [10, 20, 0, 300], [100, 200, 300, 0]]) == 2
    assert solve(5, 5, [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]) == 24


if __name__ == "__main__":
    test()
    main()
