def solve(n, m, k, c_list, a_list):
    # 色ごとに何個あるかを管理
    count_col = [0] * (m + 1)
    count_col_max = [0] * (m + 1)
    # 最初のk個
    for i in range(k):
        count_col[c_list[i]] += 1
    for c in range(m + 1):
        count_col_max[c] = count_col[c]

    # １ずつずらす
    for i in range(k, n):
        c_right = c_list[i]
        c_left = c_list[i - k]
        count_col[c_right] += 1
        count_col[c_left] -= 1
        count_col_max[c_right] = max(count_col_max[c_right], count_col[c_right])

    # 集計
    r_list = [a_list[i] * (k - count_col_max[i + 1]) for i in range(m)]
    res = min(r_list)
    return res


def main():
    n, m, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, c_list, a_list)
    print(res)


def test():
    assert solve(5, 3, 3, [1, 2, 1, 3, 2], [10, 10, 10]) == 10
    assert solve(5, 3, 3, [1, 1, 1, 1, 1], [10, 10, 10]) == 0


if __name__ == "__main__":
    test()
    main()
