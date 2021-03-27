import math
import numpy as np


def solve(n, x0, y0, x1, y1):
    base_cos = math.cos(math.pi / (n // 2))
    base_sin = math.sin(math.pi / (n // 2))
    old_add_x = (x0 - x1) / 2
    old_add_y = (y0 - y1) / 2
    new_add_x = base_cos * old_add_x - base_sin * old_add_y
    new_add_y = base_sin * old_add_x + base_cos * old_add_y

    center_x = (x0 + x1) / 2
    center_y = (y0 + y1) / 2
    return center_x + new_add_x, center_y + new_add_y


def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    res_1, res_2 = solve(n, x0, y0, x1, y1)
    print(str(res_1) + " " + str(res_2))


def test():
    assert solve(4, 1, 1, 2, 2) == (2.0, 1.0)
    # assert solve(6, 5, 3, 7, 4) == (5.93301270189, 2.38397459622)


if __name__ == "__main__":
    # test()
    main()
