def solve(n, xy_list, m, op_list, q, ab_list):
    # run
    o_list = []
    x_list = []
    y_list = []
    o = (0, 0)
    x = (1, 0)
    y = (0, 1)
    o_list.append(o)
    x_list.append(x)
    y_list.append(y)
    for op in op_list:
        if op[0] == '1':
            o = (o[1], -o[0])
            x = (x[1], -x[0])
            y = (y[1], -y[0])
        elif op[0] == '2':
            o = (-o[1], o[0])
            x = (-x[1], x[0])
            y = (-y[1], y[0])
        elif op[0] == '3':
            _, p = map(int, op.split())
            o = (2 * p - o[0], o[1])
            x = (2 * p - x[0], x[1])
            y = (2 * p - y[0], y[1])
        else:
            _, p = map(int, op.split())
            o = (o[0], 2 * p - o[1])
            x = (x[0], 2 * p - x[1])
            y = (y[0], 2 * p - y[1])
        o_list.append(o)
        x_list.append(x)
        y_list.append(y)
    # solve
    res_list = []
    for a, b in ab_list:
        xt, yt = xy_list[b - 1]
        xg = o_list[a][0] + xt * (x_list[a][0] - o_list[a][0]) + yt * (y_list[a][0] - o_list[a][0])
        yg = o_list[a][1] + xt * (x_list[a][1] - o_list[a][1]) + yt * (y_list[a][1] - o_list[a][1])
        res_list.append(str(xg) + " " + str(yg))
    # print(res_list)
    return res_list


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    op_list = [input() for _ in range(m)]
    q = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(q)]
    res_list = solve(n, xy_list, m, op_list, q, ab_list)
    for res in res_list:
        print(res)


def test():
    assert solve(
        1, [(1, 2)], 4, ["1", "3 3", "2", "4 2"], 5, [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
    ) == ["1 2", "2 -1", "4 -1", "1 4", "1 0"]


if __name__ == "__main__":
    test()
    main()
