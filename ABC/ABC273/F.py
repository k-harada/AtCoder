def solve(n, x, y_list, z_list):
    # 高橋くんの移動済範囲でグラフ的にやる
    # 現在より左か右
    point_list = [0, x] + y_list + z_list
    left_list = [0] + list(sorted([-a for a in point_list if a < 0]))
    right_list = [0] + list(sorted([a for a in point_list if a > 0]))
    # l, r, position
    d_array = [[[10 ** 18] * 2 for _1 in range(len(right_list))] for _2 in range(len(left_list))]
    d_array[0][0][0] = 0  # left
    d_array[0][0][1] = 0  # right

    walls = dict()
    for i in range(n):
        walls[y_list[i]] = i

    for i in range(len(left_list)):
        for j in range(len(right_list)):
            p = - left_list[i]
            q = right_list[j]
            if j < len(right_list) - 1:
                # 右に進む
                q2 = right_list[j + 1]
                if q2 in walls.keys():  # 壁の場合
                    if p <= z_list[walls[q2]] <= q:
                        d_array[i][j + 1][1] = min(d_array[i][j + 1][1], d_array[i][j][1] + (q2 - q))
                        d_array[i][j + 1][1] = min(d_array[i][j + 1][1], d_array[i][j][0] + (q2 - p))
                else:
                    d_array[i][j + 1][1] = min(d_array[i][j + 1][1], d_array[i][j][1] + (q2 - q))
                    d_array[i][j + 1][1] = min(d_array[i][j + 1][1], d_array[i][j][0] + (q2 - p))
            if i < len(left_list) - 1:
                # 右に進む
                p2 = - left_list[i + 1]
                if p2 in walls.keys():  # 壁の場合
                    if p <= z_list[walls[p2]] <= q:
                        d_array[i + 1][j][0] = min(d_array[i + 1][j][0], d_array[i][j][0] + (p - p2))
                        d_array[i + 1][j][0] = min(d_array[i + 1][j][0], d_array[i][j][1] + (q - p2))
                else:
                    d_array[i + 1][j][0] = min(d_array[i + 1][j][0], d_array[i][j][0] + (p - p2))
                    d_array[i + 1][j][0] = min(d_array[i + 1][j][0], d_array[i][j][1] + (q - p2))
    if x < 0:
        k = left_list.index(-x)
        res = min([d_array[k][j][0] for j in range(len(right_list))])
    else:
        k = right_list.index(x)
        res = min([d_array[i][k][1] for i in range(len(left_list))])
    if res >= 10 ** 18:
        res = -1
    return res


def main():
    n, x = map(int, input().split())
    y_list = list(map(int, input().split()))
    z_list = list(map(int, input().split()))
    res = solve(n, x, y_list, z_list)
    print(res)


def test():
    assert solve(3, 10, [-2, 8, -5], [5, -10, 3]) == 40
    assert solve(5, -1, [10, -20, 30, -40, 50], [-10, 20, -30, 40, -50]) == 1
    assert solve(1, 100, [30], [60]) == -1


if __name__ == "__main__":
    test()
    main()
