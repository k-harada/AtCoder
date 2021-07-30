def solve(n, q, xy_list, q_list):

    xy_list_add = [(x + y) for x, y in xy_list]
    xy_list_sub = [(x - y) for x, y in xy_list]
    xy_list_add_max = max(xy_list_add)
    xy_list_add_min = min(xy_list_add)
    xy_list_sub_max = max(xy_list_sub)
    xy_list_sub_min = min(xy_list_sub)

    res = []

    for i in range(q):
        q_i = q_list[i] - 1
        r = max([
            xy_list_add_max - xy_list_add[q_i], xy_list_add[q_i] - xy_list_add_min,
            xy_list_sub_max - xy_list_sub[q_i], xy_list_sub[q_i] - xy_list_sub_min
        ])
        res.append(r)

    return res


def main():
    n, q = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    q_list = [int(input()) for _ in range(q)]
    res = solve(n, q, xy_list, q_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, [(-1, 2), (1, 1), (-2, -3)], [1, 2, 3]) == [6, 7, 7]
    assert solve(5, 3, [(-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2)], [5, 3, 1]) == [8, 4, 8]
    assert solve(2, 1, [(-1000000000, -1000000000), (1000000000, 1000000000)], [1]) == [4000000000]


if __name__ == "__main__":
    test()
    main()
