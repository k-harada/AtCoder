from itertools import combinations
import numpy as np


def get_circle(x_list, y_list):

    assert len(x_list) == len(y_list)
    assert len(x_list) == 2 or len(x_list) == 3

    if len(x_list) == 3:
        a_mat = np.zeros((3, 3))
        b_vec = np.zeros(3)
        a_mat[:, 0] = x_list
        a_mat[:, 1] = y_list
        a_mat[:, 2] = 1
        b_vec[0] = x_list[0] ** 2 + y_list[0] ** 2
        b_vec[1] = x_list[1] ** 2 + y_list[1] ** 2
        b_vec[2] = x_list[2] ** 2 + y_list[2] ** 2
        try:
            circle_abc = np.linalg.solve(a_mat, b_vec)
            return circle_abc
        except np.linalg.LinAlgError:
            i, j = np.argmin(x_list), np.argmax(x_list)
            return get_circle([x_list[i], x_list[j]], [y_list[i], y_list[j]])

    else:
        a = - sum(x_list)
        b = - sum(y_list)
        x0 = x_list[0]
        y0 = y_list[0]
        c = - (x0 ** 2 + y0 ** 2 + a * x0 + b * y0)
        return np.array([a, b, c])


def judge_inner(circle_abc, x_list, y_list):
    a, b, c = circle_abc
    d_vec = np.array(x_list) ** 2 + np.array(y_list) ** 2 + a * np.array(x_list) + b * np.array(y_list) + c
    if d_vec.max() <= 0.00000001:
        return True
    else:
        return False


def get_r(circle_abc):
    a, b, c = circle_abc
    r2 = (a / 2) ** 2 + (b / 2) ** 2 - c
    return np.sqrt(r2)


def solve(n, x_list, y_list):

    res = 100000000

    for i, j, k in combinations(list(range(n)), 3):
        circle_abc = get_circle([x_list[i], x_list[j], x_list[k]], [y_list[i], y_list[j], y_list[k]])
        res_flag = judge_inner(circle_abc, x_list, y_list)
        if res_flag:
            r = get_r(circle_abc)
            res = min(res, r)

    for i, j in combinations(list(range(n)), 2):
        circle_abc = get_circle([x_list[i], x_list[j]], [y_list[i], y_list[j]])
        res_flag = judge_inner(circle_abc, x_list, y_list)
        if res_flag:
            r = get_r(circle_abc)
            res = min(res, r)
    # print(res)
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
    assert abs(solve(2, [0, 1], [0, 0]) - 0.5) < 10 ** (-6)
    assert abs(solve(3, [0, 0, 1], [0, 1, 0]) - 0.707106781186497524) < 10 ** (-6)


if __name__ == "__main__":
    test()
    main()
