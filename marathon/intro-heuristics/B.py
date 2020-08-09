import numpy as np
import numba


i4 = numba.int32


@numba.njit((i4, i4[:], i4[:, :], i4[:]), cache=True)
def solve(dd, c_arr, s_arr, t_arr):
    last_d = np.zeros(26, dtype=np.int32) - 1
    score = 0
    score_arr = np.zeros(dd, dtype=np.int32)
    for d in range(dd):
        score += s_arr[d, t_arr[d] - 1]
        last_d[t_arr[d] - 1] = d
        score -= (c_arr * (d - last_d)).sum()
        score_arr[d] = score
    return score_arr


def main():
    d = np.int32(input())
    c_arr = np.array(list(map(int, input().split()))).astype(np.int32)
    s_arr = np.array([list(map(int, input().split())) for _ in range(d)]).astype(np.int32)
    t_arr = np.array([int(input()) for _ in range(d)]).astype(np.int32)
    res = solve(d, c_arr, s_arr, t_arr)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
