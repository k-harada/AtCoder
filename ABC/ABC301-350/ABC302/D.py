from bisect import bisect_right


def solve(n, m, d, a_list, b_list):
    b_list_s = list(sorted(b_list))
    res = -1
    for a in a_list:
        j = bisect_right(b_list_s, a + d)
        if j == 0:
            continue
        else:
            b = b_list_s[j - 1]
            if b >= a - d:
                res = max(res, a + b)
    return res


def main():
    n, m, d = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, d, a_list, b_list)
    print(res)


def test():
    assert solve(2, 3, 2, [3, 10], [2, 5, 15]) == 8
    assert solve(3, 3, 0, [1, 3, 3], [6, 2, 7]) == -1
    assert solve(1, 1, 1000000000000000000,
                 [1000000000000000000], [1000000000000000000]
                 ) == 2000000000000000000
    assert solve(8, 6, 1, [2, 5, 6, 5, 2, 1, 7, 9], [7, 2, 5, 5, 2, 4]) == 14


if __name__ == "__main__":
    test()
    main()
