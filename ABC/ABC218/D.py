def solve(n, xy_list):
    res = 0
    ij_dict = dict()
    for x, y in xy_list:
        ij_dict[y] = dict()

    xy_dict = dict()
    for x, y in xy_list:
        if x not in xy_dict.keys():
            xy_dict[x] = []
        xy_dict[x].append(y)

    for x in xy_dict.keys():
        y_list = list(sorted(xy_dict[x]))
        m = len(y_list)
        for i in range(m - 1):
            a = y_list[i]
            for j in range(i + 1, m):
                b = y_list[j]
                if b not in ij_dict[a].keys():
                    ij_dict[a][b] = 1
                else:
                    ij_dict[a][b] += 1

    for a in ij_dict.keys():
        for b in ij_dict[a].keys():
            res += ij_dict[a][b] * (ij_dict[a][b] - 1) // 2

    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(6, [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]) == 3
    assert solve(4, [(0, 1), (1, 2), (2, 3), (3, 4)]) == 0
    assert solve(7, [(0, 1), (1, 0), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]) == 1


def test_large():
    print(solve(2000, [(1, i + 1) for i in range(2000)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
