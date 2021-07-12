import numpy as np
import numba


@numba.njit('Tuple((i4[:, :], i4))(i4[:, :], i4[:], i4)')
def auto_fill(res, x, bar):

    max_score = -1
    max_i = 0
    max_j = 0
    flag = 0
    for i in range(20):
        for j in range(20):
            score = 0
            for k, v in enumerate(x):
                if res[i, (j + k) % 20] == v:
                    score += 1
                elif res[i, (j + k) % 20] == 0:
                    pass
                else:
                    score -= 10000
            # print(i, j, score)
            if score > max_score:
                max_score = score
                max_i = i
                max_j = j
                flag = 1

    for i in range(20):
        for j in range(20):
            score = 0
            for k, v in enumerate(x):
                if res[(i + k) % 20, j] == v:
                    score += 1
                elif res[(i + k) % 20, j] == 0:
                    pass
                else:
                    score -= 10000
            # print(i, j, score)
            if score > max_score:
                max_score = score
                max_i = i
                max_j = j
                flag = -1
    # print(max_i, max_j, flag, max_score)
    if max_score >= bar:
        if flag == 1:
            for k, v in enumerate(x):
                res[max_i, (max_j + k) % 20] = v
        else:
            for k, v in enumerate(x):
                res[(max_i + k) % 20, max_j] = v

    return res, max_score


def solve(n, m, s_list):
    # input
    res = np.zeros((m, 20), dtype=np.int32)
    for i, s in enumerate(s_list):
        for j, c in enumerate(s):
            res[i, j] = ".ABCDEFGH".index(c)

    # greedy
    length_array = np.int32(20) * np.ones(m, dtype=np.int32)
    for i in range(m):
        for j in range(20):
            if res[i, j] == 0:
                length_array[i] = j
                break
    score_put_max = 0
    res_str = ["." * 20 for _ in range(20)]
    for _ in range(50):
        score_put = 0
        res_2 = np.zeros((20, 20), dtype=np.int32)
        length_array_noise = length_array + 0.5 * np.random.uniform(size=m)
        args = np.argsort(-length_array_noise)

        for a in args:
            if a == args[0]:
                res_2[0, :] = res[a]
                continue
            res_2, score = auto_fill(res_2, res[a, :length_array[a]], 1)
            if score > 0:
                score_put += 1
            #    print(score, res[a, :length_array[a]])
            #    print(res_2)
        # print(score_put)
        if score_put > score_put_max:
            score_put_max = score_put
            # convert
            res_str = ["".join([".ABCDEFGH"[v] for v in res_2[i, :]]) for i in range(20)]

    return res_str


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(m)]
    res_list = solve(n, m, s_list)
    for res in res_list:
        print(res)


if __name__ == "__main__":
    main()
