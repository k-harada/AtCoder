def solve(n, m, a_list):
    a_list_s = list(sorted(a_list))
    # print(a_list_s)
    r_max = 0
    s = -2
    r = 0
    for i in range(2 * n):
        if a_list_s[i % n] == s or a_list_s[i % n] == (s + 1) % m:
            r += a_list_s[i % n]
        else:
            r = a_list_s[i % n]
        s = a_list_s[i % n]
        r_max = max(r_max, r)
        # print(r)
    # print(r_max)
    if r_max >= sum(a_list):
        return 0
    else:
        return sum(a_list) - r_max


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(9, 7, [3, 0, 2, 5, 5, 3, 0, 6, 3]) == 11
    assert solve(1, 10, [4]) == 0
    assert solve(20, 20, [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]) == 99


if __name__ == "__main__":
    test()
    main()
