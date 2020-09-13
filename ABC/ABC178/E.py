def solve(n, x_list, y_list):
    # x + y
    xy_1_list = [x + y for x, y in zip(x_list, y_list)]
    # x - y
    xy_2_list = [x - y for x, y in zip(x_list, y_list)]

    res = max(max(xy_1_list) - min(xy_1_list), max(xy_2_list) - min(xy_2_list))
    return res


def main():
    n = int(input())
    x_list = [0] * n
    y_list = [0] * n
    for i in range(n):
        x, y = map(int, input().split())
        x_list[i] = x
        y_list[i] = y
    res = solve(n, x_list, y_list)
    print(res)


def test():
    assert solve(3, [1, 2, 3], [1, 4, 2]) == 4
    assert solve(2, [1, 1], [1, 1]) == 0


if __name__ == "__main__":
    test()
    main()
