def solve(n, xy_list):
    r_list = [0] * n
    r_dict = dict()
    for i, (x, y) in enumerate(xy_list):
        r = x * 1000000 + y
        r_list[i] = r
        r_dict[r] = i
    g = [[] for _ in range(n)]
    for i, r in enumerate(r_list):
        for d in [1, -1, 1000000 + 1, 1000000, 1000000 - 1, -1000000 + 1, -1000000, -1000000 - 1]:
            if r + d in r_dict.keys():
                g[i].append(r_dict[r + d])
    print(g)
    return 0


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(5, [(1, 0), (0, 1), (2, 3), (1, 2), (2, 1)]) == 0
    assert solve(0, []) == 0
    assert solve(22, [
        (0, 1), (0, 2), (0, 3), (1, 0), (1, 4),
        (2, 0), (2, 2), (2, 4), (3, 0), (3, 1),
        (3, 2), (3, 4), (5, 1), (5, 2), (5, 3),
        (6, 0), (6, 4), (7, 0), (7, 4), (8, 1),
        (8, 2), (8, 3)
    ]) == 0


if __name__ == "__main__":
    test()
    main()
