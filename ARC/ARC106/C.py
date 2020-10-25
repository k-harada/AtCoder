def solve(n, m):
    if n == 1 and m == 0:
        return ['1 2']
    if m >= n - 1:
        return [-1]
    elif m < 0:
        return [-1]
    equals_list = [f'{2 * i + 1} {2 * i + 2}' for i in range(n)]
    diff_list_pos = [f'{2000000 + 2 * i} {2000000 + 2 * i + 1}' for i in range(n)]
    diff_list_neg = [f'{2000000 + 2 * i} {2000000 + 2 * i + 1}' for i in range(n)]
    if m == 0:
        res_list = equals_list
    elif m > 0:
        res_list = diff_list_pos[:(m + 1)] + ['1000000 3000000'] + equals_list[:(n - m - 2)]
    # print(res_list)
    return res_list


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    for r in res:
        print(r)


def test():
    assert solve(5, 1) == ['2000000 2000001', '2000002 2000003', '1000000 3000000', '1 2', '3 4']
    assert solve(10, -10) == [-1]


if __name__ == "__main__":
    test()
    main()
