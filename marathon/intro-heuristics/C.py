import numpy as np
import numba


i4 = numba.int32


@numba.njit((i4, i4[:], i4[:, :], i4[:]), cache=True)
def find_before_after(x_arr, k, dd):
    # before
    for i in range(k, -1, -1):
        if x_arr[i] == 1:
            before = i
            break
    else:
        before = -1
    # after
    for i in range(k, dd):
        if x_arr[i] == 1:
            after = i
            break
    else:
        after = dd + 1
    return before, after


def solve(dd, c_arr, s_arr, t_arr, m, dq_list):
    score_delight = np.zeros(dd, dtype=np.int64)
    score_last = np.zeros(dd, dtype=np.int64)
    run_d_arr = np.zeros((dd, 26), dtype=np.int64)
    missing_d = np.zeros((dd, 26), dtype=np.int64)
    missing_d_next = np.zeros((dd, 26), dtype=np.int64) + 365

    #
    for d in range(dd):
        score_delight[d] = s_arr[d, t_arr[d]]
        run_d_arr[d, t_arr[d]] = 1

    for d in range(dd):
        if d == 0:
            missing_d[d, :] = 1
        else:
            missing_d[d, :] = missing_d[d - 1, :] + 1
        missing_d[d, t_arr[d]] = 0
        missing_d_next[:d, t_arr[d]] = np.minimum(missing_d_next[:d, t_arr[d]], d)
    score = score_d.sum() - (c_arr * missing_d).sum()

    res_list = []
    for i in range(m):
        d0_, q0_ = dq_list[i]
        d0 = d0_ - 1
        q0 = q0_ - 1
        p0 = t_arr[d0]
        # print(d0, p0, q0)
        t_arr[d0] = q0

        score += s_arr[d0, q0]
        score -= s_arr[d0, p0]
        score_d[d0] = s_arr[d0, q0]
        score += (c_arr[q0] * missing_d[:, q0]).sum()
        score += (c_arr[p0] * missing_d[:, p0]).sum()

        for d in range(dd):
            if d == 0:
                missing_d[d, p0] = 1
                missing_d[d, q0] = 1
            else:
                missing_d[d, p0] = missing_d[d - 1, p0] + 1
                missing_d[d, q0] = missing_d[d - 1, q0] + 1
            if t_arr[d] == p0:
                missing_d[d, p0] = 0
            elif t_arr[d] == q0:
                missing_d[d, q0] = 0

        score -= (c_arr[q0] * missing_d[:, q0]).sum()
        score -= (c_arr[p0] * missing_d[:, p0]).sum()

        res_list.append(score)

    return res_list


def main():
    d = np.int64(input())
    c_arr = np.array(list(map(int, input().split()))).astype(np.int64)
    s_arr = np.array([list(map(int, input().split())) for _ in range(d)]).astype(np.int64)
    t_arr = np.array([int(input()) for _ in range(d)]).astype(np.int64) - 1
    m = np.int64(input())
    dq_list = [list(map(int, input().split())) for _ in range(m)]
    res = solve(d, c_arr, s_arr, t_arr, m, dq_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
