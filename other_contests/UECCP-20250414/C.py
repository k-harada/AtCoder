from bisect import bisect_left


def solve(n, a_list, q, lr_list):
    cum_sum = [0]
    for i in range(1, n):
        if i % 2 == 1:
            cum_sum.append(cum_sum[-1])
        else:
            cum_sum.append(cum_sum[-1] + a_list[i] - a_list[i - 1])
    # print(cum_sum)
    res = []
    for left, right in lr_list:
        left_i = bisect_left(a_list, left)
        if left_i % 2 == 1:
            res_left = cum_sum[left_i]
        else:
            res_left = cum_sum[left_i] + left - a_list[left_i]
        right_i = bisect_left(a_list, right)
        # print(left_i, right_i, a_list)
        if right_i % 2 == 1:
            res_right = cum_sum[right_i]
        else:
            res_right = cum_sum[right_i] + right - a_list[right_i]
        # print(res_right, res_left)
        res.append(res_right - res_left)
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, a_list, q, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(7, [0, 240, 720, 1320, 1440, 1800, 2160], 3, [
        (480, 1920), (720, 1200), (0, 2160)
    ]) == [480, 0, 960]
    assert solve(21, [
        0, 20, 62, 192, 284, 310, 323, 324, 352, 374, 409, 452,
        486, 512, 523, 594, 677, 814, 838, 946, 1000
    ], 10, [
        (77, 721),
        (255, 541),
        (478, 970),
        (369, 466),
        (343, 541),
        (42, 165),
        (16, 618),
        (222, 592),
        (730, 983),
        (338, 747),
    ]) == [296, 150, 150, 49, 89, 20, 279, 183, 61, 177]


if __name__ == "__main__":
    test()
    main()
