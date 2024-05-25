from bisect import bisect_left

def solve(n, m, a_list):
    a_list_s = list(sorted(a_list))
    res = 0
    for i in range(n):
        r = bisect_left(a_list_s, a_list_s[i] + m) - i
        res = max(res, r)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(8, 6, [2, 3, 5, 7, 11, 13, 17, 19]) == 4
    assert solve(10, 1, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 2
    assert solve(10, 998244353, [
        100000007, 0, 1755647, 998244353, 495, 1000000000, 1755648, 503, 1755649, 998244853
    ]) == 7


if __name__ == "__main__":
    test()
    main()
