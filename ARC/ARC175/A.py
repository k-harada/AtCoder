MOD = 998244353


def solve(n, p_list, s):
    # all left or all right
    p0 = p_list[0] - 1
    used_list = [0] * n
    if s[p0] == "R":
        res_left = 0
    else:
        res_left = 1
        used_list[p0] = 1
        for i in range(1, n):
            p = p_list[i] - 1
            sp = s[p]
            # 選べる
            if used_list[(p + 1) % n] == 0:
                if sp == "R":
                    res_left *= 0
                else:
                    # sp = "L"
                    pass
            else:
                if sp == "?":
                    res_left *= 2
                    res_left %= MOD
            used_list[p] = 1

    used_list = [0] * n
    if s[p0] == "L":
        res_right = 0
    else:
        res_right = 1
        used_list[(p0 + 1) % n] = 1
        for i in range(1, n):
            p = p_list[i] - 1
            sp = s[p]
            # 選べる
            if used_list[p] == 0:
                if sp == "L":
                    res_right *= 0
                else:
                    # sp = "R"
                    pass
            else:
                if sp == "?":
                    res_right *= 2
                    res_right %= MOD
            used_list[(p + 1) % n] = 1
    res = res_left + res_right
    res %= MOD
    # print(res_left, res_right)
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    s = input()
    res = solve(n, p_list, s)
    print(res)


def test():
    assert solve(3, [1, 2, 3], "L??") == 2
    assert solve(3, [1, 3, 2], "R?L") == 0
    assert solve(12, [6, 2, 9, 3, 1, 4, 11, 5, 12, 10, 7, 8], "????????????") == 160


if __name__ == "__main__":
    test()
    main()
