def solve(n, abc_list):
    if n == 1:
        a, b, c = abc_list[0]
        return c / max(a, b)

    abc_list_s = list(sorted(abc_list, key=lambda z: z[0] / z[2]))

    curve = []

    for a, b, c in abc_list_s:
        x = a / c
        y = b / c
        # 空ならば常に追加
        if len(curve) == 0:
            curve.append((x, y))
        # それ以外はxが一致している場合以外は追加
        else:
            x0, y0 = curve[-1]
            if x == x0:
                if y < y0:
                    curve.append((x, y))
                else:
                    pass
            else:
                curve.append((x, y))
        # 除外処理
        while len(curve) >= 3:
            x2, y2 = curve.pop()
            x1, y1 = curve.pop()
            x0, y0 = curve[-1]
            pred_y2 = y1 + (x2 - x1) * (y1 - y0) / (x1 - x0)
            if pred_y2 > y2:
                curve.append((x2, y2))
            else:
                curve.append((x1, y1))
                curve.append((x2, y2))
                break

    # print(curve)

    m = len(curve)
    ind_change = -1
    for i in range(m):
        x, y = curve[i]
        if x > y:
            ind_change = i
            break
    if ind_change == 0:
        r = min([c[0] for c in curve])
    elif ind_change == -1:
        r = min([c[1] for c in curve])
    else:
        x0, y0 = curve[ind_change - 1]
        x1, y1 = curve[ind_change]
        t = (y0 - x0) / ((x1 - x0) - (y1 - y0))
        r = x0 + t * (x1 - x0)
    return 1 / r


def main():
    n = int(input())
    abc_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, abc_list)
    print(res)


def test():
    assert abs(solve(2, [(1, 2, 1), (2, 1, 1)]) - 2 / 3) < 0.00001
    assert abs(solve(1, [(500000000, 300000000, 123456789)]) - 0.246913578) < 0.00001


if __name__ == "__main__":
    test()
    main()
