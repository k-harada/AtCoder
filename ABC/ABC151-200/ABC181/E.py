from bisect import bisect_left


def solve(n, m, h_list, w_list):

    if n == 1:
        h = h_list[0]
        return min([abs(w - h) for w in w_list])

    h_list_s = list(sorted(h_list))
    # pre-compute
    # left
    left_pairs = [0] * n
    left_sum = 0
    for i in range(n):
        if i % 2 == 1:
            left_sum += h_list_s[i] - h_list_s[i - 1]
            left_pairs[i] = left_sum
    # right
    right_pairs = [0] * n
    right_sum = 0
    for i in range(n - 2, -1, -1):
        if i % 2 == 1:
            right_sum += h_list_s[i + 1] - h_list_s[i]
            right_pairs[i] = right_sum

    res = 10 ** 9 + 7
    for i in range(m):
        w = w_list[i]
        j = bisect_left(h_list_s, w)
        if j <= 1:
            r = right_pairs[1] + abs(h_list_s[0] - w)
        elif j >= n - 1:
            r = left_pairs[n - 2] + abs(h_list_s[-1] - w)
        elif j % 2 == 0:
            r = left_pairs[j - 1] + right_pairs[j + 1] + abs(h_list_s[j] - w)
        else:
            r = left_pairs[j - 2] + right_pairs[j] + abs(h_list_s[j - 1] - w)
        # print(res, r, j)
        res = min(res, r)
    return res


def main():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))
    res = solve(n, m, h_list, w_list)
    print(res)


def test():
    assert solve(5, 3, [1, 2, 3, 4, 7], [1, 3, 8]) == 3
    assert solve(7, 7, [31, 60, 84, 23, 16, 13, 32], [96, 80, 73, 76, 87, 57, 29]) == 34
    assert solve(
        15, 10, [554, 525, 541, 814, 661, 279, 668, 360, 382, 175, 833, 783, 688, 793, 736],
        [496, 732, 455, 306, 189, 207, 976, 73, 567, 759]
    ) == 239


if __name__ == "__main__":
    test()
    main()
