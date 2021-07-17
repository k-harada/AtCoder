def solve(h, w, c, a):

    dp_left_up = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            dp_left_up[i][j] = a[i][j]
            if i > 0:
                dp_left_up[i][j] = min(dp_left_up[i][j], dp_left_up[i - 1][j] + c)
            if j > 0:
                dp_left_up[i][j] = min(dp_left_up[i][j], dp_left_up[i][j - 1] + c)

    dp_left_down = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w):
            dp_left_down[i][j] = a[i][j]
            if i < h - 1:
                dp_left_down[i][j] = min(dp_left_down[i][j], dp_left_down[i + 1][j] + c)
            if j > 0:
                dp_left_down[i][j] = min(dp_left_down[i][j], dp_left_down[i][j - 1] + c)

    res = (h + w - 2) * c + a[0][0] + a[-1][-1]

    for i in range(h):
        for j in range(w):
            if i > 0:
                res = min(a[i][j] + dp_left_up[i - 1][j] + c, res)
            if i < h - 1:
                res = min(a[i][j] + dp_left_down[i + 1][j] + c, res)
            if j > 0:
                res = min(a[i][j] + min(dp_left_up[i][j - 1], dp_left_down[i][j - 1]) + c, res)
    return res


def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, c, a)
    print(res)


def test():
    assert solve(3, 4, 2, [[1, 7, 7, 9], [9, 6, 3, 7], [7, 8, 6, 4]]) == 10
    assert solve(3, 3, 1000000000, [[1000000, 1000000, 1], [1000000, 1000000, 1000000], [1, 1000000, 1000000]]) == 1001000001


if __name__ == "__main__":
    test()
    main()
