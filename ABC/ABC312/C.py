from bisect import bisect_left, bisect_right


def solve(n, m, a_list, b_list):
    res_min = 10 ** 10
    res_max = 0
    a_list_s = list(sorted(a_list))
    b_list_s = list(sorted(b_list))
    for x in a_list + b_list:
        sell = bisect_right(a_list_s, x)
        buy = m - bisect_left(b_list_s, x)
        if sell >= buy:
            res_min = min(res_min, x)
        else:
            res_max = max(res_max, x)
    # print(res_min, res_max)
    sell = bisect_right(a_list_s, res_max + 1)
    buy = m - bisect_left(b_list_s, res_max + 1)
    if sell >= buy:
        return res_max + 1
    else:
        return res_min


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 4, [110, 90, 120], [100, 80, 120, 10000]) == 110
    assert solve(5, 2, [100000, 100000, 100000, 100000, 100000], [100, 200]) == 201
    assert solve(3, 2, [100, 100, 100], [80, 120]) == 100


if __name__ == "__main__":
    test()
    main()
