LARGE = 10 ** 9 + 7


def solve(n, m, a_list, xy_list):
    max_sell = [-LARGE] * (n + 1)
    xy_list_s = list(sorted(xy_list, key=lambda xy: xy[0], reverse=True))
    for x, y in xy_list_s:
        max_sell[x] = max(max_sell[x], max(max_sell[y], a_list[y - 1]))

    res = max([max_sell[i + 1] - a_list[i] for i in range(n)])
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, a_list, xy_list)
    print(res)


def test():
    assert solve(4, 3, [2, 3, 1, 5], [(2, 4), (1, 2), (1, 3)]) == 3
    assert solve(5, 5, [13, 8, 3, 15, 18], [(2, 4), (1, 2), (4, 5), (2, 3), (1, 3)]) == 10
    assert solve(3, 1, [1, 100, 1], [(2, 3)]) == -99


if __name__ == "__main__":
    test()
    main()
