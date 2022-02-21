def solve(h, w, a):
    # 保存量を計算
    keep_h = [0] * h
    keep_w = [0] * w
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                keep_h[i] += a[i][j]
                keep_w[j] += a[i][j]
            else:
                keep_h[i] -= a[i][j]
                keep_w[j] -= a[i][j]
    # print(keep_h)
    # print(keep_w)
    # どっちを優先で埋めていくか決める
    abs_h = sum([abs(c) for c in keep_h])
    abs_w = sum([abs(c) for c in keep_w])

    new_a = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                if keep_h[i] > 0 and keep_w[j] > 0:
                    d = min(keep_h[i], keep_w[j])
                    new_a[i][j] = d
                    keep_h[i] -= d
                    keep_w[j] -= d
                elif keep_h[i] < 0 and keep_w[j] < 0:
                    d = max(keep_h[i], keep_w[j])
                    new_a[i][j] = d
                    keep_h[i] -= d
                    keep_w[j] -= d
            else:
                if keep_h[i] > 0 and keep_w[j] > 0:
                    d = min(keep_h[i], keep_w[j])
                    new_a[i][j] = -d
                    keep_h[i] -= d
                    keep_w[j] -= d
                elif keep_h[i] < 0 and keep_w[j] < 0:
                    d = max(keep_h[i], keep_w[j])
                    new_a[i][j] = -d
                    keep_h[i] -= d
                    keep_w[j] -= d
    # 最後に何か残ったら処理する
    if max(keep_h) > 0:
        for i in range(h):
            if (i % 2) == 0:
                new_a[i][0] += keep_h[i]
            else:
                new_a[i][0] -= keep_h[i]
    elif max(keep_w) > 0:
        for j in range(w):
            if (j % 2) == 0:
                new_a[0][j] += keep_w[j]
            else:
                new_a[0][j] -= keep_w[j]

    r_abs = max(abs_h, abs_w)
    res = [r_abs]
    for i in range(h):
        res.append(" ".join([str(b) for b in new_a[i]]))
    # print(res)
    return res


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a)
    for r in res:
        print(r)


def test():
    assert solve(2, 3, [[1, 2, 3], [4, 5, 6]]) == [9, "0 -3 -1", "3 0 2"]
    assert solve(2, 2, [[1000000000, -1000000000], [-1000000000, 1000000000]]) == [
        4000000000, "2000000000 0", "0 2000000000"
    ]
    assert solve(3, 4, [[0, 2, 0, -2], [-3, -1, 2, 0], [-3, -3, 2, 2]]) == [0, "0 0 0 0", "0 0 0 0", "0 0 0 0"]


if __name__ == "__main__":
    test()
    main()
