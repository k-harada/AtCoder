def solve(n, x, y, a_list):
    x2 = 0
    y2 = 0
    x_list = []
    y_list = []
    for i, a in enumerate(a_list):
        if i % 2 == 0:
            y2 += a
            y_list.append(2 * a)
        else:
            x2 += a
            x_list.append(2 * a)
    xr = x2 - x
    yr = y2 - y
    nx = len(x_list)
    ny = len(y_list)
    nx_1 = nx - nx // 2
    nx_2 = nx // 2
    ny_1 = ny - ny // 2
    ny_2 = ny // 2
    x_list_1 = x_list[:nx_1]
    x_list_2 = x_list[nx_1:]
    y_list_1 = y_list[:ny_1]
    y_list_2 = y_list[ny_1:]
    # ゴリ押し
    sx_dict_1 = dict()
    for i in range(2 ** nx_1):
        r = 0
        ii = i
        for a in x_list_1:
            if ii & 1:
                r += a
            ii >>= 1
        sx_dict_1[r] = i
    sy_dict_1 = dict()
    for i in range(2 ** ny_1):
        r = 0
        ii = i
        for a in y_list_1:
            if ii & 1:
                r += a
            ii >>= 1
        sy_dict_1[r] = i
    # print(sx_dict_1)
    # print(sy_dict_1)
    sol_x = -1
    for i in range(2 ** nx_2):
        r = 0
        ii = i
        for a in x_list_2:
            if ii & 1:
                r += a
            ii >>= 1
        if xr - r in sx_dict_1.keys():
            sol_x = sx_dict_1[xr - r] + i * (2 ** nx_1)
            break
    if sol_x < 0:
        return ["No"]

    sol_y = -1
    for i in range(2 ** ny_2):
        r = 0
        ii = i
        for a in y_list_2:
            if ii & 1:
                r += a
            ii >>= 1
        if yr - r in sy_dict_1.keys():
            sol_y = sy_dict_1[yr - r] + i * (2 ** ny_1)
            break
    if sol_y < 0:
        return ["No"]

    r = ""
    direction = "R"
    for i in range(n):
        if i % 2 == 0:
            if sol_y & 1:
                if direction == "R":
                    r += "R"
                else:
                    r += "L"
                direction = "D"
            else:
                if direction == "R":
                    r += "L"
                else:
                    r += "R"
                direction = "U"
            sol_y //= 2
        else:
            if sol_x & 1:
                if direction == "U":
                    r += "L"
                else:
                    r += "R"
                direction = "L"
            else:
                if direction == "U":
                    r += "R"
                else:
                    r += "L"
                direction = "R"
            sol_x //= 2
    # print(r)
    return ["Yes", r]


def main():
    n, x, y = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, y, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, -2, 4, [3, 2, 1]) == ["Yes", "LLR"]
    assert solve(1, 0, 0, [1]) == ["No"]
    assert solve(4, 0, 0, [1, 1, 1, 1]) == ["Yes", "RRRR"]
    assert solve(14, 2543269, -1705099, [
        3, 14, 159, 2653, 58979, 323846, 2643383, 2795028, 841971,
        69399, 37510, 58, 20, 9
    ]) == ["Yes", "LLLLLLLLLRLRRR"]


def test_large():
    print(solve(80, 0, 0, [10 ** 7] * 80))


if __name__ == "__main__":
    test()
    test_large()
    main()
