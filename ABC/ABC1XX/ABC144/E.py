def judge(n, k, a_list_s, f_list_s, v):
    res = 0
    # print(v)
    for i in range(n):
        a_necessary = v // f_list_s[i]
        # print(a_necessary, a_list_s[i])
        if a_list_s[i] > a_necessary:
            res += a_list_s[i] - a_necessary
    if res > k:
        return False
    else:
        return True


def solve_e(n, k, a_list, f_list):

    if sum(a_list) <= k:
        return 0

    a_list_s = sorted(a_list)
    f_list_s = sorted(f_list, reverse=True)

    left = 0
    right = 10 ** 12

    while right - left > 1:
        middle = (left + right) // 2
        if judge(n, k, a_list_s, f_list_s, middle):
            right = middle
        else:
            left = middle
    return right


def main():
    # input
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    f_list = list(map(int, input().split()))
    res = solve_e(n, k, a_list, f_list)
    print(res)


def test():
    assert solve_e(3, 5, [4, 2, 1], [2, 3, 1]) == 2
    assert solve_e(3, 8, [4, 2, 1], [2, 3, 1]) == 0
    assert solve_e(
        11, 14, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2]) == 12


if __name__ == "__main__":
    test()
    main()
