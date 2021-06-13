def solve(n, a_list):
    a_list_s = list(sorted(a_list))
    x = 0.0
    r_1 = sum(a_list)
    r_2 = 0.0
    res = r_1 / n
    for i in range(n):
        x = a_list_s[i] / 2
        r_1 -= a_list_s[i]
        r_2 = x * (n - 2 * (i + 1))
        r = (r_1 - r_2) / n
        # print(x, r)
        if r < res:
            res = r
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert abs(solve(3, [3, 1, 4]) - 1.83333333333333333333) < 0.000001
    assert abs(solve(10, [
        866111664, 178537096, 844917655, 218662351, 383133839, 231371336, 353498483, 865935868, 472381277, 579910117
    ]) - 362925658.1) < 0.000001


if __name__ == "__main__":
    test()
    main()
