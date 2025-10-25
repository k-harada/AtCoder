from bisect import bisect_left, bisect_right


def solve(n, x_list, p_list, q, lr_list):
    res = []
    cum_sum = [0]
    for p in p_list:
        cum_sum.append(cum_sum[-1] + p)
    for left, right in lr_list:
        left_id = bisect_left(x_list, left)
        right_id = bisect_right(x_list, right)
        res.append(cum_sum[right_id] - cum_sum[left_id])
    return res


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    p_list = list(map(int, input().split()))
    q = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, x_list, p_list, q, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 3, 5, 7], [1, 2, 3, 4], 4, [
        (1, 1), (2, 6), (0, 10), (2, 2)
    ]) == [1, 5, 10, 0]
    assert solve(7, [-10, -5, -3, -1, 0, 1, 4], [2, 5, 6, 5, 2, 1, 7], 8, [
        (-7, 7), (-1, 5), (-10, -4), (-8, 10), (-5, 0), (-10, 5), (-8, 7), (-8, -3)
    ]) == [26, 15, 7, 26, 18, 28, 26, 11]


if __name__ == "__main__":
    test()
    main()
