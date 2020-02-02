from itertools import product
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


def solve(n, m, x_list, y_list, c_list):
    d_array_base = np.zeros((n + m, n + m))
    for i in range(n + m):
        for j in range(n + m):
            d_array_base[i, j] = np.sqrt((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2)
            if c_list[i] != c_list[j]:
                d_array_base[i, j] *= 10

    res = 2000 * 35 * 10
    for p in product([0, 1], repeat=m):
        pick_list = list(range(n))
        for i in range(m):
            if p[i] == 1:
                pick_list.append(n + i)
        pick_array = np.array(pick_list)
        d_temp = d_array_base[pick_array, :][:, pick_array]
        x = csr_matrix(d_temp)
        t_csr = minimum_spanning_tree(x)
        res_temp = t_csr.toarray().sum()
        res = min(res, res_temp)

    return res


def main():
    n, m = map(int, input().split())
    x_list = [0] * (n + m)
    y_list = [0] * (n + m)
    c_list = [0] * (n + m)
    for i in range(n + m):
        x, y, c = map(int, input().split())
        x_list[i] = x
        y_list[i] = y
        c_list[i] = c
    res = solve(n, m, x_list, y_list, c_list)
    print(res)


def test():
    assert abs(solve(3, 1, [0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1]) - 2.0) < 0.000001
    assert abs(solve(3, 1, [0, 10, 10, 10], [10, 0, 20, 10], [1, 2, 3, 1]) - 210.0) < 0.000001


if __name__ == "__main__":
    test()
    main()
