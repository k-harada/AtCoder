def solve(n, k, a_list):
    a_list_s = list(sorted(a_list))
    res = a_list_s[-1] - a_list_s[0]
    # print(a_list_s)
    for i in range(k + 1):
        r = a_list_s[n - 1 - i] - a_list_s[k - i]
        res = min(res, r)
        # print(r, res)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 2, [3, 1, 5, 4, 9]) == 2
    assert solve(6, 5, [1, 1, 1, 1, 1, 1]) == 0
    assert solve(8, 3, [31, 43, 26, 6, 18, 36, 22, 13]) == 18


if __name__ == "__main__":
    test()
    main()
