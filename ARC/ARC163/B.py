def solve(n, m, a_list):
    # a_2 < a_1がめんどい
    a_list_s = list(sorted(a_list[2:]))
    res_min = 10 ** 10
    for i in range(n - 2 - m + 1):
        res = 0
        if a_list_s[i] < a_list[0]:
            res += a_list[0] - a_list_s[i]
        if a_list_s[i + m - 1] > a_list[1]:
            res += a_list_s[i + m - 1] - a_list[1]
        res_min = min(res, res_min)

    return res_min


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(3, 1, [2, 3, 5]) == 2
    assert solve(5, 2, [1, 4, 2, 3, 5]) == 0
    assert solve(8, 5, [15, 59, 64, 96, 31, 17, 88, 9]) == 35


if __name__ == "__main__":
    test()
    main()
