import numpy as np


def solve(n, s, t):
    # trim
    s_i_exist = [0] * n
    s_j_exist = [0] * n
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                s_i_exist[i] = 1
                s_j_exist[j] = 1
    s_i_exist = [i for i in range(n) if s_i_exist[i]]
    s_i_min = min(s_i_exist)
    s_i_max = max(s_i_exist)
    s_j_exist = [i for i in range(n) if s_j_exist[i]]
    s_j_min = min(s_j_exist)
    s_j_max = max(s_j_exist)

    s_trim = np.array([[s[i][j] for j in range(s_j_min, s_j_max + 1)] for i in range(s_i_min, s_i_max + 1)])

    # trim
    t_i_exist = [0] * n
    t_j_exist = [0] * n
    for i in range(n):
        for j in range(n):
            if t[i][j] == "#":
                t_i_exist[i] = 1
                t_j_exist[j] = 1
    t_i_exist = [i for i in range(n) if t_i_exist[i]]
    t_i_min = min(t_i_exist)
    t_i_max = max(t_i_exist)
    t_j_exist = [i for i in range(n) if t_j_exist[i]]
    t_j_min = min(t_j_exist)
    t_j_max = max(t_j_exist)

    t_trim = np.array([[t[i][j] for j in range(t_j_min, t_j_max + 1)] for i in range(t_i_min, t_i_max + 1)])

    # print(s_trim)
    # print(t_trim)

    # stay
    for i in range(4):
        s_rot = np.rot90(s_trim, i)
        if s_rot.shape == t_trim.shape:
            if (s_rot == t_trim).min():
                return "Yes"
    return "No"


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    res = solve(n, s, t)
    print(res)


if __name__ == "__main__":
    main()
