from bisect import bisect_left


def solve(n, a, b, d, xy_list):
    history = dict()
    loop = False
    x_now = a
    y_now = b
    d_rest = d
    direction = "right"
    xy_list_sx = list(sorted(xy_list, key=lambda xy: (xy[0], xy[1])))
    x_dict = dict()
    for x, y in xy_list_sx:
        if x not in x_dict.keys():
            x_dict[x] = [y]
        else:
            x_dict[x].append(y)
    xy_list_sy = list(sorted(xy_list, key=lambda xy: (xy[1], xy[0])))
    y_dict = dict()
    for x, y in xy_list_sx:
        if y not in y_dict.keys():
            y_dict[y] = [x]
        else:
            y_dict[y].append(x)

    while d_rest > 0:
        if direction == "right":
            if y_now not in y_dict.keys():
                x_now += d_rest
                d_rest = 0
            else:
                i = bisect_left(y_dict[y_now], x_now)
                if i == len(y_dict[y_now]):
                    x_now += d_rest
                    d_rest = 0
                else:
                    x_new = y_dict[y_now][i] - 1
                    if d_rest >= x_new - x_now:
                        d_rest -= x_new - x_now
                        x_now = x_new
                    else:
                        x_now += d_rest
                        d_rest = 0
            direction = "up"

        elif direction == "up":
            if x_now not in x_dict.keys():
                y_now += d_rest
                d_rest = 0
            else:
                i = bisect_left(x_dict[x_now], y_now)
                if i == len(x_dict[x_now]):
                    y_now += d_rest
                    d_rest = 0
                else:
                    y_new = x_dict[x_now][i] - 1
                    if d_rest >= y_new - y_now:
                        d_rest -= y_new - y_now
                        y_now = y_new
                    else:
                        y_now += d_rest
                        d_rest = 0
            direction = "left"
        elif direction == "left":
            if y_now not in y_dict.keys():
                x_now -= d_rest
                d_rest = 0
            else:
                i = bisect_left(y_dict[y_now], x_now)
                if i == 0:
                    x_now -= d_rest
                    d_rest = 0
                else:
                    x_new = y_dict[y_now][i - 1] + 1
                    if d_rest >= -(x_new - x_now):
                        d_rest -= -(x_new - x_now)
                        x_now = x_new
                    else:
                        x_now -= d_rest
                        d_rest = 0
            direction = "down"

        else:
            if x_now not in x_dict.keys():
                y_now -= d_rest
                d_rest = 0
            else:
                i = bisect_left(x_dict[x_now], y_now)
                if i == 0:
                    y_now -= d_rest
                    d_rest = 0
                else:
                    y_new = x_dict[x_now][i - 1] + 1
                    if d_rest >= -(y_new - y_now):
                        d_rest -= -(y_new - y_now)
                        y_now = y_new
                    else:
                        y_now -= d_rest
                        d_rest = 0
            direction = "right"
        key = f"{direction}_{x_now}_{y_now}"
        if key not in history:
            history[key] = d_rest
        elif not loop:
            len_loop = history[key] - d_rest
            d_rest %= len_loop
            loop = True

    return f"{x_now} {y_now}"


def main():
    res = []
    while True:
        n = int(input())
        if n == 0:
            break
        a, b, d = map(int, input().split())
        xy_list = [tuple(map(int, input().split())) for _ in range(n)]
        res.append(solve(n, a, b, d, xy_list))
    for r in res:
        print(r)


def test():
    assert solve(2, 0, 1, 4, [(3, 1), (2, 5)]) == "2 3"
    assert solve(2, 0, 1, 9, [(3, 1), (2, 5)]) == "-2 4"
    assert solve(12, 2, 2, 11, [
        (0, 1), (0, 2), (0, 3), (4, 1), (4, 2), (4, 3),
        (3, 4), (2, 4), (1, 4), (3, 0), (2, 0), (1, 0),
    ]) == "2 3"
    assert solve(12, 2, 2, 7791772263873, [
        (0, 1), (0, 2), (0, 3), (4, 1), (4, 2), (4, 3),
        (3, 4), (2, 4), (1, 4), (3, 0), (2, 0), (1, 0),
    ]) == "3 2"
    assert solve(3, 0, 3, 198, [(99, 2), (100, 3), (99, 4)]) == "0 3"
    assert solve(3, 0, 3, 1000000000000000000, [(99, 2), (100, 3), (99, 4)]) == "-999999999999999802 3"
    assert solve(1, 99, 100, 1, [(100, 100)]) == "99 101"


if __name__ == "__main__":
    test()
    main()
