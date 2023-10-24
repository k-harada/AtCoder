def solve(n, a_list):
    r = 0
    r_list = [0]
    for a in a_list:
        r += a
        r %= 360
        r_list.append(r)
    r_list_s = list(sorted(r_list)) + [360]
    # print(r_list_s)
    res = 0
    for i in range(n + 1):
        res = max(res, r_list_s[i + 1] - r_list_s[i])
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [90, 180, 45, 195]) == 120
    assert solve(1, [1]) == 359
    assert solve(10, [215, 137, 320, 339, 341, 41, 44, 18, 241, 149]) == 170


if __name__ == "__main__":
    test()
    main()
