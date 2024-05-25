import numpy as np


def solve(n, m, s):
    s_arr = np.zeros((n, m), dtype=np.int32)
    for i in range(n):
        for j in range(m):
            if s[i][j] == "#":
                s_arr[i, j] = 1
    check_arr_1 = np.array([
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1]
    ])
    check_arr_2 = np.array([
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1]
    ])
    res = []
    for i in range(n - 8):
        for j in range(m - 8):
            check = (np.abs(s_arr[i:(i + 9), j:(j + 9)] - check_arr_1) * check_arr_2).sum()
            if check == 0:
                res.append(f"{i + 1} {j + 1}")
    return res


def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    res = solve(n, m, s)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
