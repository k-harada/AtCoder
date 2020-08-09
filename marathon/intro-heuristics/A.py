import numpy as np


def solve_greedy(dd, c_arr, s_arr):
    missing_d = np.zeros(26, dtype=np.int64)
    score = 0
    res_list = []
    for d in range(dd):

        missing_d += 1

        score_add = s_arr[d, :]
        score_miss = c_arr * missing_d

        t = np.argmax(score_add + score_miss)

        score += score_add[t] + score_miss[t] - score_miss.sum()

        res_list.append(t)
        missing_d[t] = 0

    # print(score)

    return score, np.array(res_list)


def solve(dd, c_arr, s_arr):

    score, t_arr = solve_greedy(dd, c_arr, s_arr)

    score_d = np.zeros(dd, dtype=np.int64)
    missing_d = np.zeros((dd, 26), dtype=np.int64)
    for d in range(dd):
        score_d[d] = s_arr[d, t_arr[d]]
        if d == 0:
            missing_d[d, :] = 1
        else:
            missing_d[d, :] = missing_d[d - 1, :] + 1
        missing_d[d, t_arr[d]] = 0

    for i in range(1000):
        d0 = np.random.choice(dd)
        q0 = np.random.choice(26)
        p0 = t_arr[d0]
        t_arr[d0] = q0

        score_new = score

        score_new += s_arr[d0, q0]
        score_new -= s_arr[d0, p0]
        score_new += (c_arr[q0] * missing_d[:, q0]).sum()
        score_new += (c_arr[p0] * missing_d[:, p0]).sum()
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

        score_new -= (c_arr[q0] * missing_d[:, q0]).sum()
        score_new -= (c_arr[p0] * missing_d[:, p0]).sum()

        if score_new >= score:
            score = score_new
        else:
            t_arr[d0] = p0
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

    return [t + 1 for t in t_arr]


def main():
    d = np.int64(input())
    c_arr = np.array(list(map(int, input().split()))).astype(np.int64)
    s_arr = np.array([list(map(int, input().split())) for _ in range(d)]).astype(np.int64)
    res = solve(d, c_arr, s_arr)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
