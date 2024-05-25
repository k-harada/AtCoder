def solve(n, a_list):
    m = sum(a_list) // n
    res = 0
    if sum(a_list) % n == 0:
        for a in a_list:
            res += abs(a - m)
    else:
        res_1 = 0
        res_2 = 0
        for a in a_list:
            if a > m + 1:
                res_1 += a - (m + 1)
            elif a < m:
                res_2 += m - a
        res = max(res_1, res_2)

    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [4, 7, 3, 7]) == 3
    assert solve(1, [313]) == 0
    assert solve(10, [999999997, 999999999, 4, 3, 2, 4, 999999990, 8, 999999991, 999999993]) == 2499999974


if __name__ == "__main__":
    test()
    main()
