import numpy as np


def solve(n, a_array):
    v_dict = dict()
    for i in range(n):
        for j in range(6):
            v_dict[a_array[i, j]] = i
    a_array_1d = a_array.reshape((-1,))
    a_array_1d.sort()
    a_array_1d = a_array_1d[::-1]

    max_exp = 1.0

    exp_arr = np.zeros(n * 6)
    exp_arr[0] = 1.0
    for i in range(1, n * 6):
        new_exp = 1.0
        new_dice = v_dict[a_array_1d[i - 1]]
        for j in range(6):
            new_exp += exp_arr[a_array_1d.index(a_array[new_dice, j])] / 6
        max_exp = max(max_exp, new_exp)
        exp_arr[i] = max_exp

    return max_exp


def main():
    n = int(input())
    a_array = np.zeros((n, 6))
    for i in range(n):
        a6 = list(map(int, input().split()))
        for j in range(6):
            a_array[i, j] = a6[j]
    res = solve(n, a_array)
    print(res)


if __name__ == "__main__":
    main()
