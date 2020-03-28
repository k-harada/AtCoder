
def solve_base(n, a_list):
    # 2 not in a_list
    # odd or even
    factorial_count_2 = [0] * n
    for i in range(1, n):
        p = i
        cnt = 0
        while p % 2 == 0:
            p = p // 2
            cnt += 1
        factorial_count_2[i] = factorial_count_2[i - 1] + cnt

    mod_2 = 0
    for i in range(n):
        if factorial_count_2[n - 1] == factorial_count_2[i] + factorial_count_2[n - 1 - i]:
            mod_2 += a_list[i] % 2
            mod_2 %= 2

    return mod_2


def solve(n, a_list):
    if 2 in a_list:
        return solve_base(n, a_list)
    else:
        return 2 * solve_base(n - 1, [abs(a_list[i] - a_list[i + 1]) // 2 for i in range(n - 1)])


def main():
    n = int(input())
    a_list = list(map(int, list(input())))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 2, 3, 1]) == 1
    assert solve(10, [2, 3, 1, 1, 3, 1, 2, 3, 1, 2]) == 0
    # assert solve(100, [2] * 100) == 0


if __name__ == "__main__":
    test()
    main()
