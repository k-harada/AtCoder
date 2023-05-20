from bisect import bisect_left


def solve_sub(ab_list, cd_list, p):
    cd_sub_list = []
    for c, d in cd_list:
        cd_sub_list.append((c + d) * p / 100 - c)
    cd_sub_list = list(sorted(cd_sub_list))
    res = 0
    for a, b in ab_list:
        ab_add = a - (a + b) * p / 100
        res += bisect_left(cd_sub_list, ab_add)
    return res


def solve(n, m, k, ab_list, cd_list):
    left = 0.0
    right = 100.0
    for _ in range(100):
        mid = (left + right) / 2
        x = solve_sub(ab_list, cd_list, mid)
        if x >= k:
            left = mid
        else:
            right = mid
    # print(left)
    return left


def main():
    n, m, k = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    cd_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, k, ab_list, cd_list)
    print(res)


def test():
    assert abs(solve(3, 1, 1, [(1, 2), (4, 1), (1, 4)], [(1, 4)]) - 50.00) < 0.000000001
    assert abs(solve(2, 2, 2, [(6, 4), (10, 1)], [(5, 8), (9, 6)]) - 62.50) < 0.000000001
    assert abs(
        solve(4, 5, 10, [(5, 4), (1, 6), (7, 4), (9, 8)], [(2, 2), (5, 6), (6, 7), (5, 3), (8, 1)]) - 54.16666666666666
    ) < 0.000000001


if __name__ == "__main__":
    test()
    main()
