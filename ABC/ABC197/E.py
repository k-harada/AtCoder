def solve(n, xc_list):
    color_dict = dict()
    for x, c in xc_list:
        if c not in color_dict.keys():
            color_dict[c] = (x, x)
        else:
            color_dict[c] = (min(x, color_dict[c][0]), max(x, color_dict[c][1]))
    colors = list(sorted(color_dict.keys()))
    left = 0
    right = 0
    left_cost = 0
    right_cost = 0
    for c in colors:
        x_left, x_right = color_dict[c]
        # print(c, x_left, x_right, left_cost, right_cost, left, right)
        left_cost_1 = left_cost + abs(left - x_right) + (x_right - x_left)
        left_cost_2 = right_cost + abs(right - x_right) + (x_right - x_left)
        right_cost_1 = left_cost + abs(left - x_left) + (x_right - x_left)
        right_cost_2 = right_cost + abs(right - x_left) + (x_right - x_left)
        left_cost = min(left_cost_1, left_cost_2)
        right_cost = min(right_cost_1, right_cost_2)
        left = x_left
        right = x_right
    # print(c, x_left, x_right, left_cost, right_cost, right_cost, left, right)
    res = min(left_cost + abs(left), right_cost + abs(right))
    # print(res)
    return res


def main():
    n = int(input())
    xc_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xc_list)
    print(res)


def test():
    assert solve(5, [(2, 2), (3, 1), (1, 3), (4, 2), (5, 3)]) == 12
    assert solve(9, [(5, 5), (-4, 4), (4, 3), (6, 3), (-5, 5), (-3, 2), (2, 2), (3, 3), (1, 4)]) == 38


if __name__ == "__main__":
    test()
    main()
