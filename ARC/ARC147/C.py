def solve(n, lr_list):

    left_sum = 0  # 左側の内部sum
    right_sum = 0  # 右側の内部sum
    left_list = list(sorted([l for l, r in lr_list], reverse=True))
    right_list = list(sorted([r for l, r in lr_list]))
    right_max = right_list[-1]

    left_count = [0] * (right_max + 1)
    right_count = [0] * (right_max + 1)
    for l, r in lr_list:
        left_count[l] += 1
        right_count[r] += 1

    right_sum_diff = [0] * (right_max + 1)
    c = 0
    s = 0
    for le in left_list:
        right_sum += s - c * le
        right_sum_diff[le] += s - c * le
        c += 1
        s += le
    # print(right_sum)

    d_sum = right_sum
    right_c = n
    right_s = sum(left_list)
    left_c = 0
    left_s = 0

    res = d_sum

    for p in range(1, right_max + 1):
        # 右側を減らす
        right_sum -= right_sum_diff[p]
        right_s -= left_count[p] * p
        right_c -= left_count[p]
        # print(p, left_sum, right_sum, left_c, left_s, right_c, right_s)
        # d_sumを再計算
        d_sum = right_sum + left_sum
        # leftと右側
        d_sum += (p * left_c - left_s) * (n - left_c) + (right_s - p * right_c) * (n - right_c)

        if d_sum < res:
            res = d_sum
        # 左側を増やす
        left_sum += right_count[p] * (p * left_c - left_s)
        left_s += right_count[p] * p
        left_c += right_count[p]

    # print("done")
    # print(res)
    return res


def main():
    n = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, lr_list)
    print(res)


def test():
    assert solve(3, [(1, 3), (2, 4), (5, 6)]) == 4
    assert solve(3, [(1, 1), (1, 1), (1, 1)]) == 0
    assert solve(6, [(1, 5), (2, 4), (1, 1), (4, 4), (3, 6), (3, 3)]) == 15


if __name__ == "__main__":
    test()
    main()
