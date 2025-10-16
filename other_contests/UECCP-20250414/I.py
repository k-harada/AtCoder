from bisect import bisect_right


def solve(n, k, a_list):
    a_list_s = list(sorted(a_list))
    v = n
    res = 0
    d = 0
    while v > 0:
        i = bisect_right(a_list_s, v)
        v -= a_list_s[i - 1]
        if d == 0:
            res += a_list_s[i - 1]
        d = 1 - d
    # print(res)

    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(10, 2, [1, 4]) == 5
    assert solve(11, 4, [1, 2, 3, 6]) == 8
    assert solve(10000, 10, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 5136


if __name__ == "__main__":
    test()
    main()
