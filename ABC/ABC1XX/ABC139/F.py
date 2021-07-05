import math
import random
from itertools import combinations


def solve_f(n, x_list, y_list, debug=False):
    x_list_4 = [[], [], [], []]
    y_list_4 = [[], [], [], []]
    tan_theta_list_4 = [[], [], [], []]

    # tan_theta
    for i in range(n):
        x, y = x_list[i], y_list[i]
        if x >= 0 and y >= 0:  # 1st seg
            x_list_4[0].append(x)
            y_list_4[0].append(y)
            if x > 0:
                tan_theta_list_4[0].append(y / x)
            elif y > 0:
                tan_theta_list_4[0].append(10000000)
            else:
                tan_theta_list_4[0].append(0)
        elif y >= 0:  # 2st seg, x < 0
            x_list_4[1].append(x)
            y_list_4[1].append(y)
            tan_theta_list_4[1].append(y / x)
        elif x <= 0:  # 3rd seg, y < 0
            x_list_4[2].append(x)
            y_list_4[2].append(y)
            if x < 0:
                tan_theta_list_4[2].append(y / x)
            else:
                tan_theta_list_4[2].append(10000000)
        else:  # 4th seg, x > 0 and y < 0
            x_list_4[3].append(x)
            y_list_4[3].append(y)
            tan_theta_list_4[3].append(y / x)

    # sort
    x_list_sorted = []
    y_list_sorted = []
    for i in range(4):
        length = len(x_list_4[i])
        if length > 0:
            x_list_s = [(x_list_4[i][j], tan_theta_list_4[i][j]) for j in range(length)]
            y_list_s = [(y_list_4[i][j], tan_theta_list_4[i][j]) for j in range(length)]
            x_list_s.sort(key=lambda z: z[1])
            y_list_s.sort(key=lambda z: z[1])
            for j in range(length):
                x_list_sorted.append(x_list_s[j][0])
                y_list_sorted.append(y_list_s[j][0])

            if debug:
                print(x_list_s, y_list_s)
    # calc
    res = 0
    x_sum_all = sum(x_list_sorted)
    y_sum_all = sum(y_list_sorted)

    x_list_s_cumsum = [0]
    y_list_s_cumsum = [0]
    x_c = 0
    y_c = 0
    for i in range(n):
        x_c += x_list_sorted[i]
        y_c += y_list_sorted[i]
        x_list_s_cumsum.append(x_c)
        y_list_s_cumsum.append(y_c)

    for i in range(n):
        for j in range(i + 1, n + 1):
            x_sum = x_list_s_cumsum[j] - x_list_s_cumsum[i]
            y_sum = y_list_s_cumsum[j] - y_list_s_cumsum[i]
            r1 = x_sum ** 2 + y_sum ** 2
            r2 = (x_sum_all - x_sum) ** 2 + (y_sum_all - y_sum) ** 2

            res = max(res, r1, r2)

    return math.sqrt(res)


def bruce(n, x_list, y_list):
    items = list(range(n))
    subsets = []
    for i in range(len(items) + 1):
        for c in combinations(items, i):
            subsets.append(list(c))
    res = 0
    for s in subsets:
        x_sum = sum([x_list[i] for i in s])
        y_sum = sum([y_list[i] for i in s])
        r = x_sum ** 2 + y_sum ** 2
        res = max(res, r)

    return math.sqrt(res)


def test(n, trial=1000):
    for t in range(trial):
        x_list = []
        y_list = []
        for i in range(n):
            x_list.append(random.choice(range(-9, 10)))
            y_list.append(random.choice(range(-9, 10)))
        if bruce(n, x_list, y_list) != solve_f(n, x_list, y_list):
            break
    if t != trial - 1:
        print(n, x_list, y_list)
        _ = solve_f(n, x_list, y_list, True)


def main():
    n = int(input())
    x_list = [0] * n
    y_list = [0] * n
    for m in range(n):
        x, y = map(int, input().split())
        x_list[m] = x
        y_list[m] = y
    print(solve_f(n, x_list, y_list))


if __name__ == "__main__":
    # test(10)
    main()
